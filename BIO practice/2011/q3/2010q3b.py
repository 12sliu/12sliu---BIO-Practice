import copy
from time import sleep

from Upside_Down_lib import check_if_upside_down, check_if_eachnum_once

count = 0

dict = {"":(0, "123456789")}

# 0 = iteration number, 1 = remaining nums

for i in range(9):
    tempDict = {}
    for j in dict:
        if dict[j][0] == i:
            for k, number in enumerate(dict[j][1]):
                thing = copy.deepcopy(dict[j][1])
                thing = thing[:k] + thing[k+1:]
                tempDict[j+number] = (i+1, thing)
                # print(str(j)+str(number), i+1, thing)
                # sleep(0.01)
    dict.update(tempDict)
    print(i)

arr = []
for x in dict:
    if dict[x][0] == 8:
        arr.append(x)

for i in arr:
    if check_if_upside_down(int(i)):
        count += 1

print(count)
