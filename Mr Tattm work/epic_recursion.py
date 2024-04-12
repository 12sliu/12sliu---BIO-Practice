def four_dice(value, times):
    n = 0
    if times == 4:
        return 1 if value < 6 else 0
    for i in range(1, 7):
        n += four_dice(value + i, times + 1)
    return n
print(four_dice(0, 0))