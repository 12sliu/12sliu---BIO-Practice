from lib_Pentominoes import Pentominoe, shapes
from time import sleep

# target = input()

# pentA = Pentominoe(target[0])
# pentB = Pentominoe(target[1])
#
# print(pentA.get_shapes(pentB))


count = 0
setofshapes = set()
arr = []

for i in shapes:
    for j in shapes:
        if (j, i) not in setofshapes and (i, j) not in setofshapes:
            Pentominoe.existingshapes = []
            pentA = Pentominoe(i)
            pentB = Pentominoe(j)
            pentA.get_shapes(pentB)
            # pentB.get_shapes(pentA)
            value = False
            for k, shape in enumerate(pentA.existingshapes):
                if Pentominoe.check_if_internal_hole(shape):
                    value = True
                    # count += 1
                    # setofshapes.add((i, j))
                    arr.append(shape)
                    # print("k")
                    # print(shape)
            if value:
                count += 1
                setofshapes.add((i, j))

print(f"count is {count}")
print(setofshapes)

sleep(1)

for i in arr:
    print(i)
    Pentominoe.check_if_internal_hole(i)

# for i in pentA.existingshapes:
#     print(repr(i))

# 350084

"""
1:34:55 2a complete
"""
