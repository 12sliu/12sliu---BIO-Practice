from math import ceil

def check_if_upside_down(num: int):
    for i in range(ceil(len(str(num))/2)):
        if int(str(num)[i]) + int(str(num)[-i-1]) != 10:
            return False
    return True

def check_if_eachnum_once(num: int):
    e = [0 for i in range(10)]
    for i in str(num):
        e[int(i)] += 1
        # if e[int(i)] > 2 or i == "0":
        #     return False
    for i in e[1:]:
        if i != 1:
            return False
    return True


# print(check_if_eachnum_once(512396748))
