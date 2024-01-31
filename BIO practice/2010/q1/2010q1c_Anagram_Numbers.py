def check_if_anagram(num):
    arr = [0 for i in range(1, 11)]

    for i in str(num):
        arr[int(i)] = arr[int(i)] + 1

    for i in range(2, 10):
        test = num * i
        testarr = [0 for i in range(1, 11)]
        for j in str(test):
            testarr[int(j)] = testarr[int(j)] + 1
        if testarr == arr:
            return True
    return False


count = 0

for i in range(100000, 1000000):
    arr = [0 for i in range(1, 11)]
    for j in str(i):
        arr[int(j)] = arr[int(j)] + 1
    canbeadded = True
    for j in arr:
        if j > 1:
            canbeadded = False
    if canbeadded:
        if check_if_anagram(i):
            print(i)
            count += 1

print(count)

"""
Forgot to account for 0 being repeated.
0/3
"""