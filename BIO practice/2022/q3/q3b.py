from itertools import permutations

def findpark(n):
    emptyArr = ["." for _ in range(len(n))]
    badcount = 1
    for i, letter in enumerate(n):
        # print(ord(letter) - 64, emptyArr)
        emptyArr[ord(letter) - 65] = letter
        pos = ord(letter) - 66
        # print(f"pos is {pos}")
        if pos >= 0:
            while emptyArr[pos] != ".":
                pos -= 1
                # print(pos, emptyArr)
                badcount += 1
                if pos < 0:
                    break
            if badcount > 2:
                return False
    if badcount == 2:
        return True
    return False

def callfunc(q):
    arr = "".join(chr(a) for a in range(65, 65+q))
    arr2 = permutations(arr)
    count = 0
    for i in arr2:
        count += findpark(i)
    return count

for i in range(2, 8):
    print(callfunc(i))

# print(arr, len(arr))