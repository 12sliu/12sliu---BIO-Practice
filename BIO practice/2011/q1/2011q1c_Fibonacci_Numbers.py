import copy
from functools import lru_cache
from time import sleep

# print(ord("A")-64)

firstLetter, secondLetter, num = input("").split()
num = int(num)
dict = {}
arr = []

def get_next_letter(firstletter: str, secondletter: str):
    y = firstletter+secondletter
    if y not in dict:
        dict[y] = 0
    else:
        print(arr)
        print(len(arr))
        sleep(100000000)
    x = (ord(firstletter) + ord(secondletter) - 128)
    while x > 26:
        x -= 26
    return chr(x + 64)

for i in range(num -2):
    temp = copy.deepcopy(secondLetter)
    secondLetter = get_next_letter(firstLetter, secondLetter)
    firstLetter = temp
    arr.append((firstLetter, secondLetter))
    print(firstLetter, secondLetter)

print(secondLetter if num > 1 else firstLetter)

# 1000000000000000000

