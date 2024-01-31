def states_of_set(inputstate : list):

    listOfStates = {(0, 0, 0, 0, 0, 0, 0, 0)}
    finalStates = []
    currentBallCount = 0


    def _sum(arr):
        sum = 0
        for i in arr:
            sum = sum + i

        return (sum)

    for i in range(8):
        tempStates = set()
        for state in listOfStates:
            if _sum(state) == currentBallCount:
                for j in range(8):
                    newState = list(state)
                    if newState[j] < inputstate[j]:
                        newState[j] += 1
                        if tuple(newState) not in listOfStates and tuple(newState) not in tempStates:
                            tempStates.add(tuple(newState))
                            if currentBallCount == 7:
                                finalStates.append(tuple(newState))
        currentBallCount += 1
        listOfStates.update(tempStates)

    return len(finalStates)


# def bit(number):
#     return 1 if number > 0 else 0
#
#
# def pow2(number):
#     return (1 << number) & 0xffffffff
#
#
# for i in range((1 << 24) & 0xffffffff):
#     setOfPegs = []
#     for j in range(8):
#         h = 1
#         h += bit(i & pow2(3 * j + 0)) * 4
#         h += bit(i & pow2(3 * j + 1)) * 2
#         h += bit(i & pow2(3 * j + 2)) * 1
#         setOfPegs[j] = h


def dumb_recursion(pegs, curPeg):
    for i in range(8):
        pegs[curPeg] = i
        if curPeg > 0:
            if pegs[curPeg] < pegs[curPeg-1]:
                return None
        if curPeg > 7:
            print(states_of_set(pegs))
        else:
            return dumb_recursion(pegs, curPeg + 1)


dumb_recursion([0,0,0,0,0,0,0,0], 0)