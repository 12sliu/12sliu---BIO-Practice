import math
from math import sqrt, floor
#
inputNum = int(input())
#
# count = floor(math.log(inputNum, 36))
# # print(f"count is {count}")
# stringAns = ""
#
# for i in range(count):
#     newNum = inputNum // (36 - (count-i) ** count)
#     # print(f"Newnum is {newNum}")
#     inputNum = inputNum % (36 - (count-i) ** count)
#
#     if newNum == 0:
#         newNum += 1
#         # print("WARNING")
#
#     if newNum > 26:
#         stringAns = stringAns + str(newNum - 26)
#     else:
#         stringAns = stringAns + chr(newNum + 64)
#
# # if inputNum == 0:
# #     inputNum += 1
# #     print("WARNING")
#     # count -= 1
# if inputNum > 26:
#     stringAns = stringAns + str(inputNum - 26)
# else:
#     stringAns = stringAns + chr(inputNum + 64)
#
# def correct(string):
#     for i, letter in enumerate(string):
#         if letter in string[i-1:]:
#             string = add_to(string, i)
#             return correct(string)
#     return string
#
# def add_to(string, index):
#     if index < 0:
#         return correct("A" + string)
#     value = ord(string[index]) + 1
#     if value < 60:
#         if value > 10:
#             return add_to(string[index:] + "A" + string[index + 1:], index-1)
#     else:
#         if value > 90:
#             value = 0
#     return string[index:] + chr(value) + string[index + 1:]
#
# print(stringAns)

listofposs = [
    36.
]
listforposscalc = [[] for i in range(20)
]
for i in range(36):
    listforposscalc[0].append(1)

for i in range(1, 20):
    total = 0
    temp = []
    for j in range(1, 37):
        # print(sum(listforposscalc[i-1][j:]))
        total += sum(listforposscalc[i-1][j:])
        temp.append(sum(listforposscalc[i-1][j:]))
    listforposscalc[i] = temp
    # print(temp)
    # listforposscalc.append((36-i)/2.)
    # prod = 1
    # thing = 1
    # for x in listforposscalc:
    #     prod *= x
    # for y in listforposscalc[1:]:
    #     thing *= y
    # prod -= thing
    listofposs.append(total)

print(listofposs)
print(len(listforposscalc[2]))

# i = 0
# while inputNum > 0:
#     inputNum -= listofposs[i]
#     i += 1
# i -= 1
# inputNum += listofposs[i]
# ans = []
#
# print(i)

def get_ans(inputNum):
    # print(f"inputNum is {inputNum}")
    i = 0
    while inputNum > 0:
        inputNum -= listofposs[i]
        i += 1
    i -= 1
    inputNum += listofposs[i]
    ans = []
    #
    # print(i)
    # print(f"inputNum is {inputNum}")
    for place in range(i):
        value = ans[-1] if len(ans) > 0 else 0
        for k in range(value, 36):
            # sum = 1
            # for j in range(1, (i+1) - place):
            #     sum *= (36-j-place-k)
            # inputNum -= sum
            if len(ans) > 0:
                # if ans[-1]-3 < k:
                try:
                    inputNum -= listforposscalc[i-place][:][k+1]
                except IndexError:
                    pass
            else:
                inputNum -= listforposscalc[i - place][k]
            # print(inputNum, "first")
            if inputNum < 1:
                if len(ans) > 0:
                    # print(i-place, ans[-1]+1, k)
                    # print((len(listforposscalc), len(listforposscalc[i - place])))
                    inputNum += listforposscalc[i - place][:][k]
                    ans.append(k + 1)
                    # inputNum = 359
                else:
                    inputNum += listforposscalc[i - place][k]
                    ans.append(k)
                # inputNum = inputNum // sum
                # print(inputNum, "second")
                break
        # print("cont")
    # print(inputNum, ans[-1])
    if len(ans) > 0:
        ans.append(inputNum+ans[-1])
        # ans.append(inputNum+ans[-1]+(ans[0]*(i-1)))
    else:
        ans.append(inputNum-1)
    for i, thing in enumerate(ans):
        if thing < 26:
            ans[i] = chr(int(65+thing))
        else:
            ans[i] = thing - 26
    return ans

# print([(get_ans(x), x) for x in range(54000, 55000)])
print([(get_ans(x), x) for x in range(8000)])
# print(get_ans(inputNum))