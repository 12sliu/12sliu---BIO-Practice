import copy
from typing import List

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + self.suit


class Pile:

    def __init__(self, top, size):
        if type(top) == str:
            self.top = Card(top[1], top[0])
        else:
            self.top = top
        self.size = size

    def add(self, pile):
        self.top = pile.top
        self.size += pile.size

    def __str__(self):
        return f"({self.top}, {self.size})"

class CardManager:

    suits = ["C", "H", "S", "D"]
    values = ["A", "2", "3", "4", "5","6","7","8","9","T","J","Q","K"]

    def strat(self, func):
        while len(self.piles) > 1:
            if not func():
                return False
        return True

    def strat_one_update(self):
        reversePiles = self.piles[::-1]
        for i, pile1 in enumerate(reversePiles):
            for j, pile2 in enumerate(reversePiles):
                if i >= j:
                    continue
                if (pile1.top.suit == pile2.top.suit or pile1.top.value == pile2.top.value) and (abs(i - j) == 1 or abs(i-j) == 3):
                    # print("\n", pile2, pile1, reversePiles[j + i+1])
                    pile2.add(pile1)
                    reversePiles[j] = pile2
                    # print("\n", pile2, pile1, reversePiles[j+i+1])
                    reversePiles.pop(i)
                    self.piles = reversePiles[::-1]
                    # print("\n")
                    # self.print_piles()
                    return True
        self.piles = reversePiles[::-1]
        return False

    def strat_two_update(self):
        listOfMoves = []
        for i, pile1 in enumerate(self.piles):
            for j, pile2 in enumerate(self.piles):
                if i <= j:
                    break
                if (pile1.top.suit == pile2.top.suit or pile1.top.value == pile2.top.value) and (abs(i - j) == 1 or abs(i-j) == 3):
                    if len(listOfMoves) < 1:
                        pass
                    elif pile1.size + pile2.size < listOfMoves[0][0]:
                        continue
                    elif pile1.size + pile2.size > listOfMoves[0][0]:
                        listOfMoves.clear()
                    listOfMoves.append((pile1.size + pile2.size, pile1, pile2, i, j))

                    # print("\n", pile2, pile1, self.piles[j + i+1])
        if len(listOfMoves) > 0:
            listOfMoves[-1][2].add(listOfMoves[-1][1])
            self.piles[listOfMoves[-1][4]] = listOfMoves[-1][2]
            self.piles.pop(listOfMoves[-1][3])
            return True
        return False


    def strat_three_update(self):
        listOfMoves = []
        for i, pile1 in enumerate(self.piles):
            for j, pile2 in enumerate(self.piles):
                if i <= j:
                    break
                if (pile1.top.suit == pile2.top.suit or pile1.top.value == pile2.top.value) and (abs(i - j) == 1 or abs(i-j) == 3):

                    tempPiles = copy.deepcopy(self.piles)
                    tempPile1 = copy.deepcopy(pile1)
                    tempPile2 = copy.deepcopy(pile2)

                    tempPile2.add(tempPile1)
                    tempPiles[j] = tempPile2
                    tempPiles.pop(i)

                    z = self.possible_moves(tempPiles)

                    if len(listOfMoves) < 1:
                        pass
                    elif z < listOfMoves[0][0]:
                        continue
                    elif z > listOfMoves[0][0]:
                        listOfMoves.clear()
                    # print(z)
                    listOfMoves.append((z, pile1, pile2, i, j))

                    # print("\n", pile2, pile1, self.piles[j + i+1])
        if len(listOfMoves) > 0:
            listOfMoves[-1][2].add(listOfMoves[-1][1])
            self.piles[listOfMoves[-1][4]] = listOfMoves[-1][2]
            self.piles.pop(listOfMoves[-1][3])
            return True
        return False


    @staticmethod
    def possible_moves(state):
        count = 0
        iles = state
        listOfMoves = []
        for i, pile1 in enumerate(iles):
            for j, pile2 in enumerate(iles):
                if i <= j:
                    break

                if (pile1.top.suit == pile2.top.suit or pile1.top.value == pile2.top.value) and (i-j == 1 or i-j == 3):
                    count += 1
                    # print(pile1, pile2)
                # else:
                #     if pile1.top.suit == "T" and pile2.top.suit == "T":
                #         print(pile1, pile2, (pile1.top.suit == pile2.top.suit or pile1.top.value == pile2.top.value), (i-j == 1 or i-j == 3))
        return count


    def __init__(self, shufflingNums):

        self.cards = []
        self.piles = []

        for i in self.suits:
            for j in self.values:
                self.cards.append(Card(i, j))

        tempCards = []
        currentShuffleNumIndex = 0  # index

        while len(self.cards) > 0:
            currentShuffleNum = shufflingNums[currentShuffleNumIndex]
            # print("\n-------------------------------")
            # if currentShuffleNum > 0:
                # self.print_cards()
                # print(self.cards[:currentShuffleNum - 1], len(self.cards[:currentShuffleNum - 1]))
                # self.cards = self.cards + self.cards[:currentShuffleNum - 1]
                # self.print_cards()
                # print("tempcards")
                # for i in tempCards:
                #     print(i, end=" ")
                # print("tempcards")
                # print("\n", currentShuffleNum -1, len(self.cards))
                # for i in self.cards[:currentShuffleNum - 1]:
                #     print(i)
            # for i in tempCards:
            #     print(i, end=" ")
            # print()
            for i in range(currentShuffleNum - 1):
                self.cards.append(self.cards[0])
                self.cards.pop(0)
            # self.print_cards()

            tempCards.append(self.cards[0])
            self.cards.pop(0)

            currentShuffleNumIndex += 1
            if currentShuffleNumIndex > 5:
                currentShuffleNumIndex -= 6
        self.cards = tempCards
        # print("finished")
        # self.print_cards()
        self.create_piles()
        # print(tempCards)

    def create_piles(self):
        for i in self.cards:
            self.piles.append(Pile(i, 1))

    def print_cards(self):
        for i in self.cards:
            print(i, end =" ")

    def print_piles(self):
        for i in self.piles:
            print(i, end =" ")



# test = CardManager([1, 3, 5, 7, 2 ,4])

# test = CardManager([2, 11, 3, 10, 4, 9])
# test.print_cards()

# test.piles = [Pile("AD",1), Pile("8S",3), Pile("8D",1), Pile("4S",2), Pile("TH",1), Pile("KD",2), Pile("4D",2), Pile("TC",1)]
#
#
# pile1 = Pile("8D",1)
# pile2 = Pile("8S",3)
#
# tempPiles = copy.deepcopy(test.piles)
# tempPile1 = copy.deepcopy(pile1)
# tempPile2 = copy.deepcopy(pile2)
#
# tempPile2.add(tempPile1)
# tempPiles[1] = tempPile2
# tempPiles.pop(2)
#
#
# for i in tempPiles:
#     print(i, end=" ")
#
# print('BEGONE SERVANTS OF MOLOCH')
# print(CardManager.possible_moves(tempPiles))
# print('BEGONE SERVANTS OF MOLOCH')
#
# test.print_piles()
# test.strat(test.strat_three_update)
