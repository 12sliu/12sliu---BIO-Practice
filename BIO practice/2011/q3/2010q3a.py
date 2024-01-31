import time
from math import floor

from Upside_Down_lib import check_if_upside_down

# ith = int(input())
# count = 1
# upside_down_count = 0
#
# # arr = [0 for x in range(1000)]
#
# while upside_down_count < ith:
#     count += 1
#     if check_if_upside_down(count):
#         upside_down_count += 1
#         # arr[len(str(count))] += 1
#
# print(count)
# print(arr)
arr = [("5", 1)]
inp = input()
count = 1

start = time.time()

while len(arr) < int(inp):
    tempDict = []
    for num in arr:
        # print(arr)
        if num[1] == count:
            if count % 2 == 1:
                for i in range(1, 10):
                    _num = str(num[0])[:floor(len(str(num[0]))/2)] + str(num[0])[floor(len(str(num[0]))/2+1):]
                    tempDict.append((str(i) + _num + str(10 - i), count + 1))
            else:
                _num = str(num[0])[:floor(len(str(num[0])) / 2)] + "5" + str(num[0])[floor(len(str(num[0])) / 2):]
                tempDict.append((_num, count + 1))
                # print(_num)
        if len(arr) > int(inp):
            break
    count += 1
    print(count, arr[-1][0])
    arr = arr + tempDict

realarr = []
for i in arr:
    realarr.append(int(i[0]))

# print(sorted(realarr)[int(inp)-1])

realarr = sorted(realarr)
for i, num in enumerate(realarr):
    if i != 0:
        print(realarr[i]-realarr[i-1], realarr[i], realarr[i-1])
print(f"TIME IS {time.time() - start}")
print(len(realarr))

# letterarr = [0 for i in range(100)]
# for i in arr:
#     letterarr[len(i[0])] += 1
# print(letterarr)
# print(arr)

14, 68, 248, 279, 1688, 2079, 2790

# 58106 calc per second
