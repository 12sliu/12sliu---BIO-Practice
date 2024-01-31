from typing import List

baseJugCapacities = [6, 18, 20]
ans = 0

def find_possible_values(jugcapacities: List[int]):

    possibleValues = set()
    startingState = tuple(0 for i in jugcapacities)
    allStates = {startingState: 0}

    moves = 0

    while moves < 50:
        tempStates = {}
        for state in allStates:
            """
            newStateFilled = a jug is filled
            newStateEmptied = a jug is emptied
            newStatePoured = a jug is poured into another
            """

            def add_state(state):
                if tuple(state) not in tempStates and tuple(state) not in allStates:
                    tempStates[tuple(state)] = moves
                for jug in state:
                    if jug not in possibleValues:
                        possibleValues.add(jug)

            if state not in tempStates or state not in allStates:
                for i, jugA in enumerate(state):
                    newStateFilled = list(state)
                    newStateFilled[i] = jugcapacities[i]
                    add_state(newStateFilled)

                    newStateEmptied = list(state)
                    newStateEmptied[i] = 0
                    add_state(newStateEmptied)

                    for j, jugB in enumerate(state):
                        newStatePoured = list(state)
                        if i != j:
                            newStatePoured[j] += jugA
                            if newStatePoured[j] > jugcapacities[j]:
                                #
                                newStatePoured[i] = newStatePoured[j] - jugcapacities[j]
                                newStatePoured[j] = jugcapacities[j]
                            else:
                                newStatePoured[i] = 0
                            add_state(newStatePoured)
        moves += 1

        allStates.update(tempStates)

    return possibleValues

thing = find_possible_values(baseJugCapacities)

bigArr = set()

# for i in range(max(baseJugCapacities)):
#     testArr = []
#     testArr.append(i)
#     for j in range(i, max(baseJugCapacities)):
#         if j >= i:
#             testArr.append(j)
#             # bigArr.add(testArr)
#             possValues = find_possible_values(testArr)
#             print(possValues)
#             if possValues == thing:
#                 ans += 1
#             testArr = []
#             testArr.append(i)

# print(thing)


possibleNum = (max(baseJugCapacities))

for i in range(1, possibleNum ** 3):
    arr = []
    arr.append(i // (possibleNum ** 2) + 1)
    arr.append(i % (possibleNum ** 2) // (possibleNum) + 1)
    arr.append(i % possibleNum + 1)
    if arr[0] == arr[1] or arr[1] == arr[2] or arr[0] == arr[2]:
        print(f"This is triggering {arr}")
    else:
        if i > 0 and arr[0] >= arr[1] or arr[1] >= arr[2]:
            pass
        else:
            bigArr.add(tuple(arr))

print(len(bigArr))

print(thing)

for i, capacity in enumerate(bigArr):
    possValues = find_possible_values(list(capacity))
    print(i)
    if possValues == thing:
        ans += 1
        print("Hit")


print(ans)