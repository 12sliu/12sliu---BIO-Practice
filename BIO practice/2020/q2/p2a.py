class Room:
    def __init__(self, letter, start):
        self.edges = {
        }
        self.letter = letter
        self.amount = start

    def add_edge(self, letter):
        self.edges[letter] = 0

    def __eq__(self, other):
        return self.letter == other.letter


class Complex:
    rooms = []
    spylocation = None

    def __init__(self, plan):
        self.rooms = []
        letters = []
        for i in range(len(plan)+2):
            self.rooms.append(Room(chr(65+i), 1 if i == 0 else 0))
            letters.append(chr(65+i))
        self.spylocation = "A"
        # temp = []
        # for i in letters:
        #     if i not in plan:
        #         temp.append(i)
        # letters = temp
        # print(len(letters), len(plan))
        # for letter in range(len(plan)):
        count = 0
        chosen = []
        while len(plan) > 0:
            # print(ord(letter)-65, ord(letters[0])-65)
            letter = plan[0]
            if letters[0+count] in plan:
                count += 1
                continue
            self.rooms[ord((letter))-65].add_edge(letters[0+count])
            self.rooms[ord(letters[0+count])-65].add_edge(letter)
            letters.pop(0+count)
            # plan = plan[1:]
            if plan[0] not in chosen and plan[0] not in plan[1:]:
                letters.append(plan[0])
                chosen.append(plan[0])
            plan = plan[1:]
            count = 0
        self.rooms[ord(letters[1]) - 65].add_edge(letters[0])
        self.rooms[ord(letters[0]) - 65].add_edge(letters[1])

    def spy_update(self, moves):
        for move in range(moves):
            if self.letter_to_room(self.spylocation).amount % 2 == 1:
                firstletter = "["
                for letter in self.letter_to_room(self.spylocation).edges.keys():
                    if ord(letter) < ord(firstletter):
                        firstletter = letter
                self.letter_to_room(self.spylocation).edges[firstletter] += 1
                self.spylocation = firstletter
                self.letter_to_room(self.spylocation).amount += 1
            else:
                sortArray = []
                for letter in self.letter_to_room(self.spylocation).edges.keys():
                    sortArray.append(ord(letter))
                sortArray = sorted(sortArray)
                for i, ordletter in enumerate(sortArray):
                    if self.letter_to_room(self.spylocation).edges[chr(ordletter)] % 2 == 1:
                        if ordletter == sortArray[-1]:
                            self.letter_to_room(self.spylocation).edges[self.rooms[ordletter-65].letter] += 1
                            self.spylocation = self.rooms[ordletter-65].letter
                            self.letter_to_room(self.spylocation).amount += 1
                            break
                        else:
                            # print(type(self.spylocation.edges))
                            # print(sortArray[i - 1])
                            # print(self.rooms[sortArray[i-1]-65])
                            self.letter_to_room(self.spylocation).edges[self.rooms[sortArray[i-1]-65].letter] += 1
                            self.spylocation = self.rooms[sortArray[i-1]-65].letter
                            self.letter_to_room(self.spylocation).amount += 1
                            break

    def letter_to_room(self, letter):
        return self.rooms[ord(letter)-65]


n = input().split()

n[1], n[2] = int(n[1]), int(n[2])

test = Complex(n[0])

for room in test.rooms:
    # print(room.letter, end=" ")
    for i in room.edges.keys():
        print(test.rooms[ord(i)-65].letter, end="")
    # for j in room.edges.values():
    #     print(j, end=" ")
    print()

test.spy_update(n[1])
print(test.rooms[ord(test.spylocation)-65].letter, end="")
test.__init__(n[0])
test.spy_update(n[2])
print(test.rooms[ord(test.spylocation)-65].letter)


