import copy
from functools import lru_cache

a, b, c, d, n = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
n = int(n)
arr = [a, b, c, d]
ans = []

# print(arr)

tot = a + b + c + d

@lru_cache(maxsize = None)
def tree(a, b, c, d):
    if a == 0 and b == 0 and c == 0 and d == 0:
        return 1
    sum = 0
    if a > 0:
        sum += tree(a-1, b, c, d)
    if b > 0:
        sum += tree(a, b-1, c, d)
    if c > 0:
        sum += tree(a, b, c-1, d)
    if d > 0:
        sum += tree(a, b, c, d-1)
    return sum

for i in range(tot):
    count = 0
    # for j in range(len(arr)):
    #     if arr[j] > 0:
    #         arr[j] -= 1
    #         break
    while n > 0:
        temparr = copy.deepcopy(arr)
#         print(temparr)
        if temparr[count] > 0:
            temparr[count] -= 1
        else:
#             print("BREAK")
            count += 1
            continue
        n -= tree(*temparr)
#         print(tree(*temparr), temparr, n, "MARK")
#         # print(ans)
        count += 1
    n += tree(*temparr)
#     print(count - 1)
    arr[count-1] -= 1
    ans.append(count - 1)

# print(ans)
# print(tree(1, 1, 1, 0))
# 1 2 0 1
# 1 2 1 0 8

ans = [chr(i + 65) for i in ans]
print("".join(ans))

