n, i = input().split()
i = int(i)
listPossiblePreference = []
ans = []
smallestPos = 0
smallestMax = 2 ** 64
possPosPreference = []

for letter in n:
    max = 0
    maxpos = 0
    for pos, thing in enumerate(n):
        if thing == "a":
            smallestPos = pos
        if ord(thing) - 96 > max and ord(thing) - 96 < smallestMax:
            max = ord(thing) - 96
            maxpos = pos
    smallestMax = max
    possiblePreferences = 0
    while maxpos >= 0:
        maxpos -=1
        possiblePreferences += 1
        if ord(n[maxpos]) - 96 >= max:
            break
    listPossiblePreference.append(possiblePreferences)
    possPosPreference.append(maxpos + 1)

listPossiblePreference = listPossiblePreference[::-1]
listPossiblePreference = listPossiblePreference[1:]
possPosPreference = possPosPreference[::-1] # 1, 1, 0, 0
i -= 1

for pos, letter in enumerate(n):
    possValues = 1
    for j in listPossiblePreference[pos:]:
        possValues *= j
    count = 0
    while i >= possValues:
        i -= possValues
        count+= 1
    ans.append(possPosPreference[pos] + count)
print("".join(chr(num + 65) for num in ans))



# # n, i = "cabd", 5
# n, i = input().split()
# i = int(i)
#
# listPossiblePreference = []
#
# ans = []
# smallestPos = 0
# smallestMax = 2 ** 64
# possPosPreference = []
#
# for letter in n:
#
#     max = 0
#     maxpos = 0
#     for pos, thing in enumerate(n):
#         if thing == "a":
#             smallestPos = pos
#         if ord(thing) - 96 > max and ord(thing) - 96 < smallestMax:
#             max = ord(thing) - 96
#             maxpos = pos
#     smallestMax = max
#     possiblePreferences = 0
#     while maxpos >= 0:
#         maxpos -=1
#         possiblePreferences += 1
#         if ord(n[maxpos]) - 96 >= max:
#             break
#     listPossiblePreference.append(possiblePreferences)
#     possPosPreference.append(maxpos + 1)
#
# listPossiblePreference = listPossiblePreference[::-1]
# listPossiblePreference = listPossiblePreference[1:]
# # listPossiblePreference.append(1)
#
# possPosPreference = possPosPreference[::-1] # 1, 1, 0, 0
#
# # print(ans, listPossiblePreference, possPosPreference)
# i -= 1
#
# for pos, letter in enumerate(n):
#     possValues = 1
#     for j in listPossiblePreference[pos:]:
#         possValues *= j
#
#     count = 0
# #     print(i)
#     while i >= possValues:
#         i -= possValues
#         count+= 1
#     ans.append(possPosPreference[pos] + count)
# #     print(possValues, listPossiblePreference[pos:], count)
#
# # print(ans)
#
# print("".join(chr(num + 65) for num in ans))
# # 1 2 0 0
