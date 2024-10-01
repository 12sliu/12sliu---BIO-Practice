# count = 1
# while count < 11:
#     print(count)
#     count +=1
#
# print("\n".join([str(i) for i in range(11)]))

from typing import Tuple
from copy import copy
import time
from typing import Iterable


def convert_to_tuple(two_dimensional_list):
    return tuple([tuple(sublist) for sublist in two_dimensional_list])


def convert_to_list(two_dimensional_tuple):
    return list([list(subtuple) for subtuple in two_dimensional_tuple])


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def check_if_in_bounds(self):
        return 0 <= self.x < 4 and 0 <= self.y < 5

    def __str__(self):
        return f"Point "

class Size(Point):
    pass


class Block:
    def __init__(self, size: Size, coords: Point, count):
        self.size = size
        self.coords = coords
        self.count = count

    def __str__(self):
        return f"Block {self.count} of size {self.size}, at {self.coords}"

class BlockFill:

    def __init__(self, block: Block):
        self.block = block

    def __str__(self):
        return f"Blockfill: Block: {self.block}"

class RedBlock(Block):
    pass


class Manager:

    grid = [[None for _ in range(4)] for _ in range(5)]
    redPosition = Point(1, 0)

    savedTestingGrid = None

    saved_coords = [
        {
            "coords": Point(0, 0), # coords is x and y
            "size": Size(1, 2) # x size and y size
        },
        {
            "coords": Point(3, 0),
            "size": Size(1, 2)
        },
        {
            "coords": Point(0, 2),
            "size": Size(1, 2)
        },
        {
            "coords": Point(3, 2),
            "size": Size(1, 2)
        },
        {
            "coords": Point(1, 2),
            "size": Size(2, 1)
        },
        {
            "coords": Point(0, 4),
            "size": Size(1, 1)
        },
        {
            "coords": Point(3, 4),
            "size": Size(1, 1)
        },
        {
            "coords": Point(2, 3),
            "size": Size(1, 1)
        },
        {
            "coords": Point(1, 3),
            "size": Size(1, 1)
        }
    ]

    def __init__(self):
        count = 0
        for i in self.saved_coords:
            count += 1
            print(i["coords"].x, i["coords"].y)
            self.grid[i["coords"].y][i["coords"].x] = Block(i["size"], i["coords"], count)
        self.grid[self.redPosition.y][self.redPosition.x] = RedBlock(Size(2, 2), Point(1, 0), "R")

    def print_grid(self, inputgrid):
        printGrid = [[None for _ in range(4)] for _ in range(5)]
        count = 1
        for line in inputgrid:
            for tile in line:
                if tile is not None:
                    for blockPartY in range(tile.size.y):
                        for blockPartX in range(tile.size.x):
                            try:
                                printGrid[blockPartY+tile.coords.y][blockPartX+tile.coords.x] = tile.count
                            except IndexError:
                                print("whattttttttttttttt", blockPartY, blockPartX, tile.coords, tile.size, tile.count, inputgrid)

                    count += 1
        for line in printGrid:
            for tile in line:
                if tile is None:
                    print("0 ", end = "")
                else:
                    print(f"{tile} ", end = "")
            print()

    def print_self_grid(self):
        self.print_grid(self.grid)

    def move_red(self, targetRedPosition: Point):
        starttime = time.time()
        count = 0

        seedState = convert_to_tuple(self.grid)

        existentStates = set(convert_to_tuple(self.grid))
        queues = [[seedState], []]  # amazingly stupid queue system, new queues are created every iteration
        # there will be 200 empty lists after 200 iterations
        # too bad

        memocount = 0
        howmanystates = 0
        for iterations in range(1000):
            testingGrid = None
            for state in queues[count]:
                howmanystates += 1
                checkList = set()  # the set of blocks that need to be checked if they can move into the empty space
                blockMoveVectors = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]
                emptySpaceCheckVectors = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1), Point(-2, 0), Point(0, -2)]

                # set all the tiles with something in it to 1
                newgrid = [[None for _ in range(4)] for _ in range(5)]
                for line in state:
                    for tile in line:
                        if tile is not None:
                            for blockPartY in range(tile.size.y):
                                for blockPartX in range(tile.size.x):
                                    newgrid[blockPartY + tile.coords.y][blockPartX + tile.coords.x] = 1

                # find all tiles with 0, check tiles for blocks that could move to the 0 tile
                # more efficient than checking and testing every single block
                for pointY, line in enumerate(newgrid):
                    for pointX, point in enumerate(line):
                        if point is None:
                            for vector in emptySpaceCheckVectors:
                                testPoint = Point(pointX+vector.x, pointY+vector.y)
                                if not testPoint.check_if_in_bounds():
                                    continue
                                if state[testPoint.y][testPoint.x] is not None:
                                    checkList.add(Point(testPoint.x, testPoint.y))

                # go through the blocks that could move to a 0 tile
                # and then start testing if they can move
                for blockPoint in checkList:
                    for blockMoveVector in blockMoveVectors:
                        testPoint = Point(blockPoint.x+blockMoveVector.x, blockPoint.y+blockMoveVector.y)
                        if not testPoint.check_if_in_bounds():
                            continue
                        elif state[testPoint.y][testPoint.x] is not None:
                            continue

                        # really complicated way to just move a block in one of four directions
                        testingGrid = convert_to_list(state)
                        testingGrid[testPoint.y][testPoint.x] = copy(state[blockPoint.y][blockPoint.x])
                        testingGrid[blockPoint.y][blockPoint.x] = None
                        testingGrid[testPoint.y][testPoint.x].coords = testPoint

                        # memorization
                        hashgrid = self.make_hashable_grid(testingGrid)
                        if hashgrid in existentStates:
                            memocount += 1
                            continue

                        if self.test_grid(testingGrid,
                                          testPoint):
                            if isinstance(testingGrid[testPoint.y][testPoint.x], RedBlock):
                                if testPoint == targetRedPosition:
                                    self.print_grid(testingGrid)
                                    return True
                            queues[count+1].append(convert_to_tuple(testingGrid))
                            existentStates.add(hashgrid)
            print(f"on iteration {count+1}")
            print(f"time is {time.time() - starttime}")
            print(f"{howmanystates} states processed")
            print(f"{memocount} states ignored")
            print(len(existentStates))
            self.print_grid(testingGrid)
            howmanystates = 0
            queues.append([])
            queues[count] = []
            count += 1
        return False

    def make_hashable_grid(self, grid):
        newgrid = [[None for _ in range(4)] for _ in range(5)]
        for line in grid:
            for tile in line:
                if tile is not None:
                    newgrid[tile.coords.y][tile.coords.x] = tile.count
        return convert_to_tuple(newgrid)

    def test_grid(self, testgrid, newcoords: Point):
        newgrid = [[None for _ in range(4)] for _ in range(5)]
        count = 1
        movedpiece = testgrid[newcoords.y][newcoords.x]
        for line in testgrid[max(newcoords.y-1, 0):min(newcoords.y+movedpiece.size.y + 1, 5)]:
            for tile in line[max(newcoords.x-1, 0):min(newcoords.x+movedpiece.size.x + 1, 4)]:
                if tile is not None:
                    for blockPartY in range(tile.size.y):
                        for blockPartX in range(tile.size.x):
                            blockPartAbsPos: Point = Point(blockPartX + tile.coords.x, blockPartY + tile.coords.y)
                            if not blockPartAbsPos.check_if_in_bounds() or newgrid[blockPartAbsPos.y][blockPartAbsPos.x] is not None:
                                return False
                            newgrid[blockPartAbsPos.y][blockPartAbsPos.x] = tile.count
                    count += 1
        self.savedTestingGrid = newgrid
        return True


thing = Manager()
thing.print_self_grid()
thing.move_red(Point(1, 3))