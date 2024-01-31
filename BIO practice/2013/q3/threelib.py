import copy
from math import ceil
import random


class System:
    keypad, sample = [
        [0 for x in range(5)],
        [0 for x in range(5)],
        [0 for x in range(5)],
        [0 for x in range(5)],
        [0 for x in range(5)]
    ],[
        [0 for x in range(5)],
        [0 for x in range(5)],
        [0 for x in range(5)],
        [0 for x in range(5)],
        [0 for x in range(5)]
    ]

    def __init__(self, buttonString):

        for i in buttonString:
            thing = ord(i) - 64
            value = 2
            if thing > 26:
                value = 1
                thing -= 32
            y = (thing - 1) // 5
            x = thing % 5 - 1
            # print(y, x, thing, i)
            self.keypad[y][x] = value

        # for i, row in enumerate(self.keypad):
        #     self.keypad[i] = tuple(row)
        # for i, row in enumerate(self.sample):
        #     self.sample[i] = tuple(row)
        # self.sample = tuple(self.sample)
        # self.keypad = tuple(self.keypad)

    def solve(self):
        # dictionary = {"": copy.deepcopy(self.sample)}
        # count = 0
        ans = []
        for i in range(200):
            listOfMoves = []
            for i, row in enumerate(self.sample):
                for j, key in enumerate(row):
                    # tempSample = list(copy.deepcopy(self.sample))
                    # for k, row2 in enumerate(self.sample):
                    #     self.sample[k] = list(row2)
                    # if key == self.keypad[i][j]:
                    #     print(key)
                    #     continue
                    # print(state + chr(96 + i * 5 + j + 1))
                    # if i != 0:
                    #     if self.keypad[i-1][j] >= self.sample[i-1][j]:
                    #         continue
                    # if j != 0:
                    #     if self.keypad[i][j-1] >= self.sample[i][j-1]:
                    #         continue
                    # if i != 4:
                    #     if self.keypad[i+1][j] >= self.sample[i+1][j]:
                    #         continue
                    # if j != 4:
                    #     if self.keypad[i][j+1] >= self.sample[i][j+1]:
                    #
                    #       continue
                    if key != self.keypad[i][j]:
                        listOfMoves.append((i, j))
            i, j = listOfMoves[random.randint(0, len(listOfMoves)-1)]
            print(self.sample, i, j, self.keypad)
            if i != 0:
                self.sample[i - 1][j] = (self.sample[i - 1][j] + 1) % 3
                # print(self.sample, "first")
            if i != 4:
                self.sample[i + 1][j] = (self.sample[i + 1][j] + 1) % 3
#                 print(self.sample, "second")
            if j != 0:
                self.sample[i][j - 1] = (self.sample[i][j - 1] + 1) % 3
#                 print(self.sample, "third")
            if j != 4:
                self.sample[i][j + 1] = (self.sample[i][j + 1] + 1) % 3
#                 print(self.sample, "fourth")
            self.sample[i][j] = (self.sample[i][j] + 1) % 3
#             print(self.sample, "fifth")
            # for k, row2 in enumerate(tempSample):
            #     tempSample[k] = tuple(row2)

            if self.sample == self.keypad:
                return self.compress(reversed("".join(ans) + chr(96 + i * 5 + j + 1)))
            else:
                ans.append(chr(96 + i * 5 + j + 1))
                    # tempdict[state + chr(96 + i * 5 + j + 1)] = tuple(tempSample)
            # tempdict = {}
            # print(len(dictionary))
            # for state in dictionary:
            #     # print(state, "state", count)
            #     if len(state) == count:
            #         # print(self.keypad, self.sample)
            #         # for i in self.keypad:
            #         #     print(i)
            #         for i, row in enumerate(self.keypad):
            #             for j, key in enumerate(row):
            #                 tempSample = list(copy.deepcopy(dictionary[state]))
            #                 for k, row2 in enumerate(tempSample):
            #                     tempSample[k] = list(row2)
            #                 # if key == self.keypad[i][j]:
            #                 #     print(key)
            #                 #     continue
            #                 # print(state + chr(96 + i * 5 + j + 1))
            #                 # if i != 0:
            #                 #     if self.keypad[i-1][j] >= self.sample[i-1][j]:
            #                 #         continue
            #                 # if j != 0:
            #                 #     if self.keypad[i][j-1] >= self.sample[i][j-1]:
            #                 #         continue
            #                 # if i != 4:
            #                 #     if self.keypad[i+1][j] >= self.sample[i+1][j]:
            #                 #         continue
            #                 # if j != 4:
            #                 #     if self.keypad[i][j+1] >= self.sample[i][j+1]:
            #                 #         continue
            #                 try:
            #                     tempSample[i-1][j] = (tempSample[i-1][j] + 1) % 3
            #                 except IndexError:
            #                     pass
            #                 try:
            #                     tempSample[i+1][j] = (tempSample[i+1][j] + 1) % 3
            #                 except IndexError:
            #                     pass
            #                 try:
            #                     tempSample[i][j-1] = (tempSample[i][j-1] + 1) % 3
            #                 except IndexError:
            #                     pass
            #                 try:
            #                     tempSample[i][j+1] = (tempSample[i][j+1] + 1) % 3
            #                 except IndexError:
            #                     pass
            #                 tempSample[i][j] = tempSample[i][j] + 1 % 3
            #                 for k, row2 in enumerate(tempSample):
            #                     tempSample[k] = tuple(row2)
            #                 if tempSample == self.keypad:
            #                     return self.compress("".join(reversed(state + chr(96+i*5+j+1))))
            #                 tempdict[state + chr(96+i*5+j+1)] = tuple(tempSample)
            #         # if self.sample == lastSample:
            #         #     return None
            # dictionary.update(tempdict)
            # count += 1
        # return self.compress("".join(reversed(ans)))
        return None

    def compress(self, string):
        thing = ""
        for i, letter in enumerate(string):
            if letter == thing:
                return self.compress(string[:i-1] + chr(ord(letter)-32) + string[i+1:])
            thing = letter
        return string
