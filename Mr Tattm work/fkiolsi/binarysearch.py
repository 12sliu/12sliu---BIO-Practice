sortedList = [2,2,2,2,2,2,2,3,3,3,54,5,6,4,5,4,53,4,4,3,4,3,8]
sortedList.sort()
target = 8
leftPointer, rightPointer = 0, len(sortedList)
while True:
    midpoint = (leftPointer + rightPointer) // 2
    midpointValue = sortedList[midpoint]
    if midpointValue == target:
        print(sortedList[midpoint])
        break
    if target > midpointValue:
        leftPointer = midpoint-1
    else:
        rightPointer = midpoint+1
    if leftPointer + 1 == rightPointer:
        print(sortedList[midpoint + 1])
        break
