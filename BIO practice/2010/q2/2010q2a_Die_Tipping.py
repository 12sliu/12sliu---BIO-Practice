from typing import List


def print_grid(pos, grid):
    size = 0
    for i in range(pos[0] - (1 + size), pos[0] + (2 + size)):
        for j in range(pos[1] - (1 + size), pos[1] + (2 + size)):
            # TODO: This should have been >=. Lost a third of the marks to this.
            if 10 > i > 0 and 10 > j > 0:
                print(grid.get_grid()[i][j], end="")
                # print(grid.get_grid()[i][j], end=f" {[i, j]} ")
            else:
                print("x", end="")
        print("\n")
    pass

class Grid:

    grid = []

    def __init__(self, inp):
        self.grid = [[1 for j in range(11)] for i in range(11)]
        for i in range(4, 7):
            for j in range(4, 7):
                self.grid[i][j] = int(inp[i-4][j-4])

    def get_location(self, location: List[int]):
        return self.grid[location[0]][location[1]]

    def set_location(self, location: List[int], value):
        self.grid[location[0]][location[1]] = value

    def get_grid(self):
        return self.grid


class Dice:

    left = 3
    up = 2
    high = 1

    heading = 0

    location = [5, 5]

    def __init__(self, grid: Grid):
        self.grid = grid

    def move(self, num):
        for i in range(num):
            # value = (self.grid.get_location(self.location) + self.high) % 6 \
            #     if (self.grid.get_location(self.location) + self.high) % 6 != 0 else 1

            if (self.grid.get_location(self.location) + self.high) <= 6:
                value = (self.grid.get_location(self.location) + self.high)
                # print(f"{self.grid.get_location(self.location)} + {self.high} is {value}")
                # print(f"left is {self.left}, up is {self.up}")
            else:
                value = (self.grid.get_location(self.location) + self.high) - 6
            #     print("value is 1")
            # print(f"CALCULATING")

            grid.set_location(self.location, value)

            if value == 3 or value == 4:
                self.heading += 2
            if value == 2:
                self.heading += 1
            if value == 5:
                self.heading -= 1
            while self.heading > 3:
                self.heading -= 4
            while self.heading < 0:
                self.heading += 4
            self.move_with_heading(value)

    def move_with_heading(self, value):
        if self.heading == 0:
            self.location[0] = self.location[0] - 1

            tempup = self.high
            temphigh = 7 - self.up

            self.high = temphigh
            self.up = tempup
        elif self.heading == 1:
            self.location[1] = self.location[1] + 1

            templeft = 7 - self.high
            temphigh = self.left

            self.high = temphigh
            self.left = templeft
        elif self.heading == 2:
            self.location[0] = self.location[0] + 1

            tempup = 7 - self.high
            temphigh = self.up

            self.high = temphigh
            self.up = tempup
        elif self.heading == 3:
            self.location[1] = self.location[1] - 1

            templeft = self.high
            temphigh = 7 - self.left

            self.high = temphigh
            self.left = templeft

        if self.location[0] < 0:
            self.location[0] = 10
        if self.location[1] < 0:
            self.location[1] = 10
        if self.location[0] > 10:
            self.location[0] = 0
        if self.location[1] > 10:
            self.location[1] = 0

        # print(self.location)
        # print(f"high is {self.high}")
        # print(f"grid value is {self.grid.get_location(self.location)}")
        # print(f"value is {value}")
        # print(f"heading is {self.heading}")
        # print_grid(self.get_dice_pos(), self.grid)

    def get_dice_pos(self):
        return self.location


grid = Grid([input().split() for i in range(3)])
# print(grid.get_grid())
#
# print(grid.get_location([5, 5]))
# for i in range(pos[0]-2, pos[0]+1):
#     for j in range(pos[1]-2, pos[1]+1):
#         if 10 > i > 0 and 10 > j > 0:
#             print(grid.get_grid()[i][j], end="")
#         else:
#             print("x", end="")
#     print("\n")

dice = Dice(grid)
dice.move(int(input()))

def driver():
    print_grid(dice.get_dice_pos(), grid)


    thing = int(input())
    # print(thing)
    if thing != 0:
        # print("what")
        dice.move(thing)
        driver()

driver()

"""
4.5 hours(roughly)

2(a) 
Test 1 = 3/3
Test 2 = 0/2
Test 3 = 5/5
Test 4 = 2/7
Test 5 = 2/7

2(b) = 2/2
2(c) = 0/4
2(d) = 0/5

Total = 14/35
"""