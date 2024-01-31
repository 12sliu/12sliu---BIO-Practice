alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p, q, r = [int(x) for x in input().split()]
inputNum = int(input())


def gen_formula(beforenum, count):
    lm = r - count
    if count+1 < r:
        return 0
    print(f"lm is {lm}")

    array = [1]
    i = 1
    while lm > len(array):
        value = p ** (i + beforenum)
        for j in range(1, i):
            value += array[len(array)-1-j] * (p-1)
        array.append(value)
        i += 1
        # print(len(array))
        # print(lm < len(array), lm)
    return array[-1]


def build(ans, n, length):
    if length < 1:
        return ans
    num = 0
    i = 0
    while n > num:
        value = p ** length
        # adj = False
        count = 1
        for i in range(1, q):
            if len(ans) > i + 1:
                if ans[-1-i] == ans[-1]:
                    count += 1
        print(value)
        value -= gen_formula(count, length)
        # if count == q:
        #     adj = True
        # if adj:
        #     value *= (p-1)/p
        # print(value, n)
        print(value, ans + alpha[i], n, length - 1)
        # i += 1
        if value >= n:
            return build(ans + alpha[i], n, length - 1)
        n -= value
        i += 1
    return build(ans+alpha[i], n, length-1)


print([build("", x, r) for x in range(1, 10)])
