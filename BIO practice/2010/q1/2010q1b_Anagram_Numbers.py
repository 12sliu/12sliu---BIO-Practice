def anagram_generations(num):
    arr = [0 for i in range(1, 10)]
    ans = []

    for i in str(num):
        arr[int(i)-1] = arr[int(i)-1] + 1

    for i in range(2, 10):
        test = num * i
        testarr = [0 for i in range(1, 10)]
        for j in str(test):
            testarr[int(j)-1] = testarr[int(j)-1] + 1
        if testarr == arr:
            ans.append(test)
    return ans

num = 85247910
numarr = [0 for i in range(1, 10)]
for i in str(num):
    numarr[int(i) -1 ] = numarr[int(i)-1] + 1

for i in range(10000000, 100000000):
    iarr = [0 for i in range(1, 10)]
    for j in str(i):
        iarr[int(j) - 1] = iarr[int(j) - 1] + 1
    if iarr == numarr:
        arr = anagram_generations(i)
        for j in arr:
            if j == num:
                print(i)

"""
28 minutes to complete 1a to 1c - assume that I'm going to do Q2 while waiting on this.
31:47 finished running

2/2

"""