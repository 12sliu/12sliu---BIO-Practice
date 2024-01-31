import copy
import math
from math import floor

# list = [i for i in range(1, 100000, 2)]
# marked = 1
# curNum = 1
inputNum = int(input())
listOfLucky = [i for i in range(1, 10100, 2)]
oddCount = 1
#
# while curNum < inputNum:
#     luckyNum = list[marked]
#     curNum = list[marked]
#     for i in range(floor(100000/luckyNum)):
#         list.pop(((i+1)*luckyNum)-1)
#     marked += 1
i = 1
while i < len(listOfLucky):
    # k = 1
    j = 1
    value = listOfLucky[i]
    temp = copy.deepcopy(listOfLucky)
    while value * j-j < len(temp):
        # if len(listOfLucky) < value * j:
        temp.pop(value * j - j )
        j += 1
        # else:
        #     break
    # while j < len(listOfLucky):
    #     k += 1
    #     if k > listOfLucky[i]:
    #         k = 0
    #         listOfLucky.pop(j)
    #     j += 1
    listOfLucky = temp
    i += 1

print(len(listOfLucky))
print(listOfLucky)
for i, number in enumerate(listOfLucky):
    if number > inputNum:
        # print(number, end=" ")
        j = i
        while listOfLucky[j] >= inputNum:
            j -= 1
        print(listOfLucky[j], number)
        break
    # if math.ceil(oddCount / 2) not in listOfLucky:
    #     listOfLucky.append(oddCount)
    # oddCount += 2

# print(len([1, 3, 7, 9, 11, 15, 19, 23, 25, 27, 31, 33, 35, 39, 41, 43, 47, 51, 55, 57, 59, 63, 67, 71, 73, 75, 79, 83, 87, 89, 91, 95, 97, 99]))
# print(listOfLucky[-2] if listOfLucky[-2] < inputNum else listOfLucky[-3], listOfLucky[-1])


# print(list[marked-1], list[marked])

# Test 2, 3, 4, 5, 6, 7, 8
