from lib_Accordion_Patience import CardManager

ans = set()

for i in range(10 ** 6):
    nums = [
        i % (10 ** 1) // (10 ** 0) + 1,
        i % (10 ** 2) // (10 ** 1) + 1,
        i % (10 ** 3) // (10 ** 2) + 1,
        i % (10 ** 4) // (10 ** 3) + 1,
        i % (10 ** 5) // (10 ** 4) + 1,
        i % (10 ** 6) // (10 ** 5) + 1
    ]
    ans.add(frozenset(x.__str__() for x in CardManager(nums).cards[:6]))

print(len(ans))
# 531431
# 998284
