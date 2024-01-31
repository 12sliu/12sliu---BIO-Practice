import math
from math import floor

# list = [i for i in range(1, 100000, 2)]
# marked = 1
# curNum = 1
# inputNum = int(input())
listOfLucky = {1}
oddCount = 1
#
# while curNum < inputNum:
#     luckyNum = list[marked]
#     curNum = list[marked]
#     for i in range(floor(100000/luckyNum)):
#         list.pop(((i+1)*luckyNum)-1)
#     marked += 1

lastNum = 0

while len(listOfLucky) < 1000000000:
# while len(listOfLucky) < 100:
    if math.ceil(oddCount / 2) not in listOfLucky:
        listOfLucky.add(oddCount)
        lastNum = oddCount
    oddCount += 2
    if len(listOfLucky) % 1000000 == 0:
        print(len(listOfLucky))


# print(listOfLucky)
print(lastNum)

# print(len([1, 3, 7, 9, 11, 15, 19, 23, 25, 27, 31, 33, 35, 39, 41, 43, 47, 51, 55, 57, 59, 63, 67, 71, 73, 75, 79, 83, 87, 89, 91, 95, 97, 99]))
# print(listOfLucky[-2] if listOfLucky[-2] < inputNum else listOfLucky[-3], listOfLucky[-1])


# print(list[marked-1], list[marked])
