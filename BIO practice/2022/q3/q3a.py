n, i = input().split()

listPossiblePreference = []

ans = []
smallestPos = 0
smallestMax = 2 ** 64

for letter in n:

    max = 0
    maxpos = 0
    for i, thing in enumerate(n):
        if thing == "a":
            smallestPos = i
        if ord(thing) - 96 > max and ord(thing) - 96 < smallestMax:
            max = ord(thing) - 96
            maxpos = i
    smallestMax = max
    print(max, maxpos)
    possiblePreferences = 0
    while maxpos >= 0:
        maxpos -=1
        possiblePreferences += 1
        if ord(n[maxpos]) - 96 >= max:
            break
    listPossiblePreference.append(possiblePreferences)

listPossiblePreference = listPossiblePreference[::-1]
listPossiblePreference = listPossiblePreference[1:]

ans.append(smallestPos)
print(ans, listPossiblePreference)

for i, letter in enumerate(n):
    possValues = 1
    for j in n[i+1:]:
        possValues *= j

