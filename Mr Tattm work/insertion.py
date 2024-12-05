iList = [6, 5, 4, 3, 2, 1]

for i in range(len(iList)):
    print(iList, "iList")
    for j in range(len(iList[0:i+1])):
        if iList[j] > iList[i]:
            iList.insert(j, iList[i])
            iList.pop(i+1)
            break

print(iList)