# count = 1
# while count < 11:
#     print(count)
#     count +=1
#
# print("\n".join([str(i) for i in range(11)]))

from typing import Tuple
from copy import copy

class Block:
    def __init__(self, size: Tuple[int, int], coords: Tuple[int, int], count):
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
    red_coords = (1, 0)

    saved_coords = [
        {
            "coords": (0, 0), # coords is x and y
            "size": (1, 2) # x size and y size
        },
        {
            "coords": (3, 0),
            "size": (1, 2)
        },
        {
            "coords": (0, 2),
            "size": (1, 2)
        },
        {
            "coords": (3, 2),
            "size": (1, 2)
        },
        {
            "coords": (1, 2),
            "size": (2, 1)
        },
        {
            "coords": (0, 4),
            "size": (1, 1)
        },
        {
            "coords": (3, 4),
            "size": (1, 1)
        },
        {
            "coords": (2, 3),
            "size": (1, 1)
        },
        {
            "coords": (1, 3),
            "size": (1, 1)
        }
    ]

    def __init__(self):
        count = 0
        for i in self.saved_coords:
            count += 1
            self.grid[i["coords"][1]][i["coords"][0]] = Block( i["size"], i["coords"], count)
        self.grid[0][1] = RedBlock((2, 2), (1, 0), "R")

    def print(self, grid):
        newgrid = [[None for _ in range(4)] for _ in range(5)]
        count = 1
        for line in grid:
            for i in line:
                if i is not None:
                    for j in range(i.size[1]):
                        for k in range(i.size[0]):
                            newgrid[j+i.coords[1]][k+i.coords[0]] = i.count
                    count += 1
        for line in newgrid:
            for tile in line:
                if tile is None:
                    print("0 ", end = "")
                else:
                    print(f"{tile} ", end = "")
            print()

    def print_self(self):
        self.print(self.grid)

    def move_red(self, pos: Tuple[int, int]):
        statesdict = {tuple([tuple(i) for i in self.grid]): 0}
        count = 0
        howmanystates = 0
        tempdict = {}
        for i in range(100):
            for state in statesdict:
                if statesdict[state] == count:
                    howmanystates += 1
                    for i, line in enumerate(state):
                        for j, point in enumerate(line):
                            if point is not None:
                                thingjiggy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                                for k in thingjiggy:
                                    if not(0 <= i+k[0] < 5 and 0 <= j+k[1] < 4):
                                        continue
                                    elif state[i+k[0]][j+k[1]] is not None:
                                        continue
                                    newnewgrid = copy(list(list(i) for i in state))
                                    # print(f"\n {point.count}")
                                    newnewgrid[i+k[0]][j+k[1]] = copy(state[i][j])
                                    newnewgrid[i][j] = None
                                    newnewgrid[i + k[0]][j + k[1]].coords = (j + k[1], i + k[0])
                                    self.print(state)
                                    if self.test_grid(newnewgrid, (i + k[0], j + k[1])):
                                        # self.print(newnewgrid)
                                        # print()
                                        # print()
                                        if isinstance(state[i][j], RedBlock):
                                            if (j + k[1], i + k[0]) == pos:
                                                return 0
                                        tempdict[tuple([tuple(i) for i in newnewgrid])] = count + 1
            statesdict.update(tempdict)
            print(count)
            print(howmanystates)
            howmanystates = 0
            count += 1

    def test_grid(self, testgrid, newcoords):
        newgrid = [[None for _ in range(4)] for _ in range(5)]
        count = 1
        movedpiece = testgrid[newcoords[0]][ newcoords[1]]
        for line in testgrid[max(newcoords[0]-1, 0):min(newcoords[0]+movedpiece.size[0] + 1, 5)]:
            for i in line[max(newcoords[1]-1, 0):min(newcoords[1]+movedpiece.size[1] + 1, 4)]:
                if i is not None:
                    for j in range(i.size[1]):
                        for k in range(i.size[0]):
                            if not(0 <= j + i.coords[1] < 5 and 0 <= k + i.coords[0] < 4):
                                return False
                            if newgrid[j + i.coords[1]][k + i.coords[0]] is not None:
                                # print(newgrid, (j + i.coords[1],k + i.coords[0]), i.count)
                                # print("broken!")
                                return False
                            newgrid[j + i.coords[1]][k + i.coords[0]] = i.count
                    # print(newgrid)
                    count += 1
        # print(testgrid)
        print(newgrid, newcoords)
        movedpiece = testgrid[newcoords[0]][ newcoords[1]]
        print(max(newcoords[0]-1, 0), min(newcoords[0]+movedpiece.size[0], 4))
        print(max(newcoords[1]-1, 0), min(newcoords[1]+movedpiece.size[1], 3))
        for line in testgrid[max(newcoords[0]-1, 0):min(newcoords[0]+movedpiece.size[0] + 1, 5)]:
            for i in line[max(newcoords[1]-1, 0):min(newcoords[1]+movedpiece.size[1] + 1, 4)]:
                print(i)
                print("hhhh")
        self.print(testgrid)
        print("above should be testgrid")
        return True


thing = Manager()
thing.print_self()
thing.move_red((1, 3))