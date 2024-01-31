# startingState = ("1", "2", "3", "4")
# endingState = ("2", "3", "4", "1")

startingState = tuple(input().split())
endingState = tuple(input().split())
print(startingState, endingState)

allStates = {startingState: 0}


def find_move():
    global allStates
    currentMoves = 0

    if startingState == endingState:
        return 0

    while currentMoves < 12:
        tempStates = {}

        print(len(allStates))

        # if currentMoves == 3:
        #     print(allStates)

        # iterate through all states
        for state in allStates:
            stateMoves = allStates[state]
            # checks if the State is a leaf
            if stateMoves == currentMoves:
                # iterates through the four pegs
                for i, currentPeg in enumerate(state):
                    # checks if the peg is empty
                    lastCharacterOfCurrentPeg = str(currentPeg)[-1]
                    if lastCharacterOfCurrentPeg != "0":
                        # adds it to the other three states
                        for j, addPeg in enumerate(state):
                            if i != j:
                                # turns inmutable tuple into mutable list
                                lst = list(state)
                                # adds the top ball to a peg
                                if addPeg != "0":
                                    lst[j] = str(addPeg) + lastCharacterOfCurrentPeg
                                else:
                                    lst[j] = lastCharacterOfCurrentPeg

                                # removes the top ball from the current peg
                                lst[i] = str(lst[i])[:-1]
                                if len(lst[i]) == 0:
                                    lst[i] = "0"
                                # adds it to the list of possible states
                                if not tuple(lst) in allStates and not tuple(lst) in tempStates:
                                    if tuple(lst) == endingState:
                                        print(tuple(lst), currentMoves + 1, "\n", state)
                                        return currentMoves + 1
                                    else:
                                        # if currentMoves == 1:
                                        #   print(tuple(lst), currentMoves + 1, "\n", state)
                                        tempStates[tuple(lst)] = currentMoves + 1


        currentMoves += 1
        allStates.update(tempStates)

    return None


# print(moves)
print(find_move())

# print("Welcome to the CPU quiz!")
# print("Q1: What organ could the CPU be compared to?\n[a] Arms [b] Brain or [c] Heart")
# answer = input("Please choose a, b, or c:")
# if answer == "b":
#     print("Correct")
# elif answer == "c" or answer == "a":
#     print("Wrong")
# else:
#     print("invalid")

