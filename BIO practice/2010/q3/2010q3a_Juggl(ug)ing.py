numJugs, requiredAmount = input().split()
jugCapacities = list(input().split())

# intelligent code yes I am smart
for i, thing in enumerate(jugCapacities):
    jugCapacities[i] = int(thing)
numJugs = int(numJugs)
requiredAmount = int(requiredAmount)

startingState = tuple(0 for i in jugCapacities)

allStates = {startingState: 0}

def find_moves(requiredamount):
    if requiredamount == 0:
        return 0

    for jug in jugCapacities:
        if jug == requiredamount:
            return 1

    moves = 0

    while moves < 1000:
        tempStates = {}
        for state in allStates:
            """
            newStateFilled = a jug is filled
            newStateEmptied = a jug is emptied
            newStatePoured = a jug is poured into another
            """
            if state not in tempStates or state not in allStates:
                for i, jugA in enumerate(state):
                    newStateFilled = list(state)
                    newStateFilled[i] = jugCapacities[i]
                    if tuple(newStateFilled) not in tempStates and tuple(newStateFilled) not in allStates:
                        tempStates[tuple(newStateFilled)] = moves

                    newStateEmptied = list(state)
                    newStateEmptied[i] = 0
                    if tuple(newStateEmptied) not in tempStates and tuple(newStateEmptied) not in allStates:
                        tempStates[tuple(newStateEmptied)] = moves

                    for j, jugB in enumerate(state):
                        newStatePoured = list(state)
                        if i != j:
                            newStatePoured[j] += jugA
                            if newStatePoured[j] > jugCapacities[j]:
                                #
                                newStatePoured[i] = newStatePoured[j] - jugCapacities[j]
                                newStatePoured[j] = jugCapacities[j]
                            else:
                                newStatePoured[i] = 0
                            if tuple(newStatePoured) not in tempStates and tuple(newStatePoured) not in allStates:
                                tempStates[tuple(newStatePoured)] = moves
                                print(tuple(newStatePoured), state)
        moves += 1

        allStates.update(tempStates)

        for state in allStates:
            for jug in state:
                if jug == requiredamount:
                    print(state)
                    return moves



print(find_moves(requiredAmount))
