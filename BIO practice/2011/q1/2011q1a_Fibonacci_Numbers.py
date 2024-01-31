import copy
from functools import lru_cache

# print(ord("A")-64)

firstLetter, secondLetter, num = input("").split()
num = int(num)

def get_next_letter(firstletter: str, secondletter: str):
    x = (ord(firstletter) + ord(secondletter) - 128)
    while x > 26:
        x -= 26
    return chr(x + 64)

for i in range(num -2):
    temp = copy.deepcopy(secondLetter)
    secondLetter = get_next_letter(firstLetter, secondLetter)
    firstLetter = temp
    # print(firstLetter, secondLetter)

print(secondLetter if num > 1 else firstLetter)

# 1000000000000000000
# 33:36 done, full marks!!!!!!!!!!!!
