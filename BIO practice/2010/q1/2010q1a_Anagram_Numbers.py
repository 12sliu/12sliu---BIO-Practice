num = int(input())
arr = [0 for i in range(1, 10)]

for i in str(num):
    arr[int(i) -1 ] = arr[int(i)-1] + 1
# print(arr)
isAna = False

for i in range(2, 10):
    test = num * i
    testarr = [0 for i in range(1, 10)]
    for j in str(test):
        testarr[int(j)-1] = testarr[int(j)-1] + 1
    # print(testarr)
    if testarr == arr:
        print(i)
        isAna = True

if not isAna:
    print("NO")

"""
Test 6 failed
23/25
"""