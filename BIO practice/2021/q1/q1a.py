n = input()

def get_highest_value(string):
    highest = 0
    for i in string:
        if ord(i) > highest:
            highest = ord(i)
    return highest

def get_lowest_value(string):
    lowest = 9999999
    for i in string:
        if ord(i) < lowest:
            lowest = ord(i)
    return lowest


def check_if_pat(string):
    ans = []
    if len(string) == 1:
        return True
    for i in range(1, len(n)):
        str1, str2 = n[:i], n[i:]
        print(str1, str2, str1[::-1])
        if get_lowest_value(str1) > get_highest_value(str2):
            print("WGAT")
            ans.append(check_if_pat(str1[::-1]) and check_if_pat(str2[::-1]))
    print(ans)
    return sum(ans)


print(check_if_pat(n))
