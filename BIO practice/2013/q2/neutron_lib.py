import copy


class Neutron:
    def __init__(self, location):
        self.location = location

class Piece(Neutron):
    def __init__(self, location, number, player):
        super().__init__(location)
        self.number = number
        self.player = player

class Board:
    board = [[None for x in range(5)],
             [None for x in range(5)],
             [None for x in range(5)],
             [None for x in range(5)],
             [None for x in range(5)]]

    p1order = []
    p2order = []

    p1pieces = [Piece([4, x], x, 1) for x in range(5)]
    p2pieces = [Piece([0, x], x, 2) for x in range(5)]
    neutron = Neutron([2, 2])

    nextpturn = 1

    def __init__(self, p1order, p2order):
        self.p1order = p1order
        self.p2order = p2order

        self.board[4] = [x for x in self.p1pieces]
        self.board[0] = [x for x in self.p2pieces]
        self.board[2] = [None, None, self.neutron,None,None]

    def update(self):
        print("NEW TURN JUST DROPPED\n\n\n")
        if self.nextpturn == 1:
            self.nextpturn = 2
            return self.pupdate(1, 0, self.board)
            # self.nextpturn = 2
        else:
            self.nextpturn = 1
            return self.pupdate(2, 0, self.board)

    def pupdate(self, player, neutronCount, prevboard):

        # badMoves = []

        # for direction in range(1, 9):
        # chosenPiece = copy.deepcopy(
        #   self.p1pieces[self.p1order[0] - 1] if player == 1 else self.p2pieces[self.p2order[0] - 1])
        #     tempBoard = copy.deepcopy(self.board)
        #     while 0 <= chosenPiece.location[0] < 5 and 0 <= chosenPiece.location[1] < 5:
        #         self.movepiece(chosenPiece, direction)
        #         if 0 <= chosenPiece.location[0] < 5 and 0 <= chosenPiece.location[1] < 5:
        #             if tempBoard[chosenPiece.location[0]][chosenPiece.location[1]] is not None:
        #                 break
        #             else:
        #                 badMoves.append([chosenPiece.location[0],chosenPiece.location[1]])

        # for i in badMoves:
#             print(i, end=" ")
#         print()
#         print(f"Neutron is at {self.neutron.location}")

        # badMoves.append([chosenPiece.location[0]-1, chosenPiece.location[1]-1])
        # badMoves.append([chosenPiece.location[0]+1, chosenPiece.location[1]-1])
        # badMoves.append([chosenPiece.location[0]-1, chosenPiece.location[1]+1])
        # badMoves.append([chosenPiece.location[0]+1, chosenPiece.location[1]+1])
        self.board = prevboard
        listOfEndMoves = []
        listOfMoves = []
        changedNeutron = False
        for i in range(8):
            tempBoard, neutronLocation = self.get_next_state(True, 0, 0, i + 1)
            if neutronLocation != self.neutron.location:
                listOfMoves.append((tempBoard, neutronLocation))
                if player == 1:
                    if neutronLocation[0] == 4:
                        self.board = tempBoard
                        return 1
                    if neutronLocation[0] == 0:
                        listOfEndMoves.append(tempBoard)
                        # print(tempBoard)
                        listOfMoves.pop(-1)
                else:
                    if neutronLocation[0] == 0:
                        self.board = tempBoard
                        return 2
                    if neutronLocation[0] == 4:
                        listOfEndMoves.append(tempBoard)
                        # print(tempBoard)
                        listOfMoves.pop(-1)
            # changedNeutron = True
        # print(self.p1order[0])

        if not changedNeutron and 0 == len(listOfMoves) and len(listOfEndMoves) > 0:
            self.board = listOfEndMoves[0]
            return 2 if player == 1 else 1
        elif not changedNeutron and 0 == len(listOfMoves):
            return 3

        count = 0

        for i in listOfMoves:
            if i[1] != self.neutron.location:
                if count < neutronCount:
                    count += 1
                    continue
                # self.board[self.neutron.location[0]][self.neutron.location[1]] = None
                # self.board[i[1][0]][i[1][1]] = self.neutron
                prevBoard = copy.deepcopy(self.board)
                prevNeutronLocation = self.neutron.location
                self.board = i[0]
                print("NEUTRON CHANGED", i[1], self.neutron.location)
                self.neutron.location = i[1]
                break

        regularMoves = []

        print(len(self.p1pieces), len(self.p2pieces))
        for i in self.p1pieces:
            print(i.location, i.player)
        if player == 1:
            for i in range(8):
                tempBoard, pieceLocation = self.get_next_state(False, self.p1order[0]-1, player, i + 1)
                if pieceLocation != self.p1pieces[self.p1order[0]-1].location:
                    # self.p1pieces[self.p1order[0] - 1].location = pieceLocation
                    regularMoves.append((pieceLocation, tempBoard))
                    print(f"i is {i}")
                    break
        elif player == 2:
            for i in range(8):
                tempBoard, pieceLocation = self.get_next_state(False, self.p2order[0]-1, player, i + 1)
                if pieceLocation != self.p2pieces[self.p2order[0]-1].location:
                    # self.p2pieces[self.p2order[0] - 1].location = pieceLocation
                    regularMoves.append((pieceLocation, tempBoard))
                    break

        if len(regularMoves) == 0:
            print("MADE IN HEAVEN")
            self.print_board_state(prevBoard)
            self.neutron.location = prevNeutronLocation
            self.pupdate(player, neutronCount + 1, prevBoard)
            # self.neutron.location = prevNeutronLocation
        else:
            self.board = regularMoves[0][1]
            if player == 1:
                self.p1pieces[self.p1order[0] - 1].location = pieceLocation
                self.p1order.append(self.p1order.pop(0))
            elif player == 2:
                self.p2pieces[self.p2order[0] - 1].location = pieceLocation
                self.p2order.append(self.p2order.pop(0))

        return 0


    def print_board_state(self, board):
        for i in board:
            for j in i:
                if isinstance(j, Piece):
                    print(f"F{j.number} " if j.player == 1 else f"S{j.number} ", end="")
                elif isinstance(j, Neutron):
                    print("*  ", end = "")
                else:
                    print(".  ", end="")
            print()
        print()
        # print(f"Neutron is at {self.neutron.location}")

    def print_state(self):
        self.print_board_state(self.board)


    def get_next_state(self, isneutron, number, player, direction):
        tempBoard = copy.deepcopy(self.board)
        if isneutron:
            piece = copy.deepcopy(self.neutron)
        else:
            piece = copy.deepcopy(self.p1pieces[number] if player == 1 else self.p2pieces[number])
        # print(piece.location[0], piece.location[1], isneutron)
        tempBoard[piece.location[0]][piece.location[1]] = None
#         print(tempBoard[piece.location[0]][piece.location[1]] is None and 0 <= piece.location[0] < 5 and 0 <= piece.location[1] < 5)
        while 0 <= piece.location[0] < 5 and 0 <= piece.location[1] < 5:
            self.movepiece(piece, direction)
            if 0 <= piece.location[0] < 5 and 0 <= piece.location[1] < 5:
                if direction == 8:
                    save = tempBoard[piece.location[0]][piece.location[1]]
                    tempBoard[piece.location[0]][piece.location[1]] = piece
                    print("DIRECITON IS 8, BEHOLD")
                    if isinstance(piece, Piece):
                        print(piece.number, piece.player)
                    self.print_board_state(tempBoard)
                    tempBoard[piece.location[0]][piece.location[1]] = save
                if tempBoard[piece.location[0]][piece.location[1]] is not None:
                    break
        tempBoard[piece.location[0]][piece.location[1]] = self.movepiece(piece, direction + 4 if direction + 4 < 9 else direction - 4)
        return [tempBoard, piece.location]

    def movepiece(self, piece, direction):
        match direction:
            case 1:
                piece.location[0] -= 1
            case 2:
                piece.location[0] -= 1
                piece.location[1] += 1
            case 3:
                piece.location[1] += 1
            case 4:
                piece.location[0] += 1
                piece.location[1] += 1
            case 5:
                piece.location[0] += 1
            case 6:
                piece.location[0] += 1
                piece.location[1] -= 1
            case 7:
                piece.location[1] -= 1
            case 8:
                piece.location[0] -= 1
                piece.location[1] -= 1
        return piece





# test = Board(1, 1)
