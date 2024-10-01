import copy

original_table = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

answer_table = [
    [12, 10, 11, 9],
    [16, 14, 5, 13],
    [8, 6, 7, 15],
    [4, 2, 3, 1]
]

print(original_table)

def swap_row(table, index):
    newtable = copy.deepcopy(table)
    newtable[index] = table[index+1]
    print(f"got it, {table}")
    newtable[index+1] = table[index]
    return newtable

def swap_column(table, index):
    newtable = copy.deepcopy(table)
    for i in range(4):
        newtable[i][index] = table[i][index+1]
        newtable[i][index+1] = table[i][index]
    return newtable


def tuple_to_list(inputtuple):
    return list([list(i) for i in inputtuple])


def list_to_tuple(inputlist):
    return tuple([tuple(i) for i in inputlist])

print (list_to_tuple(original_table))
allStates = {list_to_tuple(original_table): 0}

def find_move():
    global allStates
    currentMoves = 0

    if original_table == answer_table:
        return 0

    while currentMoves < 100:
        tempStates = {}

        print(len(allStates))

        # if currentMoves == 3:
        #     print(allStates)

        # iterate through all states
        for state in allStates:
            stateMoves = allStates[state]
            # checks if the State is a leaf
            if stateMoves == currentMoves:
                # adds it to the list of possible states
                def add_state(lst):
                    print(lst)
                    if not list_to_tuple(lst) in allStates and not list_to_tuple(lst) in tempStates:
                        if lst == answer_table:
                            print(lst, currentMoves + 1, "\n", state)
                            return currentMoves + 1
                        else:
                            tempStates[list_to_tuple(lst)] = currentMoves + 1

                state_table = tuple_to_list(state)
                for i in range(3):
                    add_state(swap_column(state_table, i))
                    add_state(swap_row(state_table, i))
        currentMoves += 1
        allStates.update(tempStates)
        print(currentMoves, len(allStates))
    return None

find_move()

