tileArray = {
    1: [1, 2, 1, 2],
    2: [2, 1, 2, 1],
    3: [1, 2, 2, 1],
    4: [1, 1, 2, 2],
    5: [2, 1, 1, 2],
    6: [2, 2, 1, 1],
}

class Tile:

    def __init__(self, tilerepr, grid, gridsize, coordinates):
        self.sides = tilerepr
        self.grid = grid
        self.gridsize = gridsize
        self.coordinates = coordinates

    def check(self):
        n = [
            (self.coordinates[0]-1, self.coordinates[1]),
            (self.coordinates[0], self.coordinates[1]+1),
            (self.coordinates[0]+1, self.coordinates[1]),
            (self.coordinates[0], self.coordinates[1]-1)
        ]
        for i, side in enumerate(self.sides):
            if self.coordinates == (1, 0):
                print(n[i], self.coordinates)
            if 0 <= n[i][0] < self.gridsize and 0 <= n[i][1] < self.gridsize:
                if self.coordinates == (1, 0):
                    print("ACTIVATE", self.coordinates)
                otherTile = self.grid.grid[n[i][0]][n[i][1]]
                otherTile.recursive_check(i, self, 1, self.sides[i])



    def recursive_check(self, direction_from, origin, length, colour):
        for looper in self.grid.listOfLoopers[colour-1]:
            if looper.coordinates == self.coordinates:
                return
        if origin.coordinates == self.coordinates:
            self.grid.ppoint[colour-1] += length
            self.grid.listOfLoopers[colour-1].append(self)
            if origin == (1, 0):
                print("SUCCESS", self.coordinates)
            return
        curSide = direction_from + 2
        curSide = curSide - 4 if curSide >= 4 else curSide
        if self.sides[curSide] == colour:
            if origin.coordinates == (1, 0):
                print("side is good colour")
            n = [
                (self.coordinates[0]-1, self.coordinates[1]),
                (self.coordinates[0], self.coordinates[1]+1),
                (self.coordinates[0]+1, self.coordinates[1]),
                (self.coordinates[0], self.coordinates[1]-1)
            ]
            for i, side in enumerate(self.sides):
                if i == curSide:
                    continue
                if 0 <= n[i][0] < self.gridsize and 0 <= n[i][1] < self.gridsize and side == colour:
                    print("recursive")
                    self.grid.grid[n[i][0]][n[i][1]].recursive_check(i, origin, length + 1, colour)
        else:
            if origin.coordinates == (1, 0):
                print("side is bad colour", self.sides, curSide)


class Grid:

    grid = []
    ppoint = [0, 0]
    listOfLoopers = [[], []]

    def __init__(self, size, gridrepr):
        for i in range(size):
            self.grid.append([Tile(tileArray[gridrepr[i][j]], self, size,(i, j)) for j in range(size)])

        for row in self.grid:
            for tile in row:
                tile.check()


size = int(input())

inputArray = [
    [int(x) for x in input().split()] for i in range(size)
]

test = Grid(size, inputArray)
print(test.ppoint)

# Test
