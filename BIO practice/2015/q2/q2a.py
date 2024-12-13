# arr = [0, 1, 2]
# print(arr[0:2])
a, c, m = [int(i) for i in input().split()]

r = 0

board = [[0 for i in range(10)] for j in range(10)]

def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))

def check_valid(x1, x2, y1, y2):
    x1 = clamp(0, x1, 10)
    x2 = clamp(0, x2, 10)
    y1 = clamp(0, y1, 10)
    y2 = clamp(0, y2, 10)
    print(x1, x2, y1, y2)
    # # print(board[9][4])
    # # print(board[x1:x2])
    for i in board[x1:x2]:
        for j in i[y1:y2]:
            # j = 1
            if j == 1:
# #                 print("FALSE", i)
                return False
    return True

#  x = 5, y = 1
# r = 5, r = 55, r = 555, r = 5555


def place_ship(ship):
    global r
    placed = False
    x, y = 0, 0
    h = False
    while not placed:
        r = (a * r + c) % m
# #         print(r)
        rstr = "000" + str(r)
        x = int(rstr[-1])
        y = int(rstr[-2])
        r = (a * r + c) % m
# #         print(r)
        if r % 2 == 1:
            if y + ship -1 < 10:
                if check_valid(x -1, x+2, y -1, y + ship + 1):
                    for i in range(ship):
                        board[x][y+i] = 1
                    placed = True

        else:
            if x + ship - 1 < 10:
                if check_valid(x -1, x+ship+1, y -1, y + 2):
                    for i in range(ship):
                        board[x+i][y] = 1
                    placed = True
                    h = True
    print(x, y, "H" if h else "V")


# for i in range(10, 0, -1):
#     for row in board:
#         print(row[i])

arr = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
# print(arr[0:2])
for i in arr:
    place_ship(i)
    for i in range(9, -1, -1):
        for row in board:
            print(row[i], end = " ")
        print()





