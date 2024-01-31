import copy
from lib_Pentominoes import Pentominoe, shapes

target = ["L", "I", "V"]

pentA = Pentominoe(target[0])
pentB = Pentominoe(target[1])
pentC = Pentominoe(target[2])

count = 0

print(pentB.get_shapes(pentA))
print(pentA.get_shapes(pentB))
# print(len(pentA.existingshapes))

iterator = copy.deepcopy(Pentominoe.existingshapes)

Pentominoe.existingshapes = []

for i, shape in enumerate(iterator):
    print(shape)
    pentominoe = Pentominoe("V", shape=shape)
    print(i, pentominoe.get_shapes(pentC))
    # arr1 = copy.deepcopy(Pentominoe.existingshapes)

    # pentominoe.existingshapes = []

    print(i, pentC.get_shapes(pentominoe))
    # arr2 = copy.deepcopy(Pentominoe.existingshapes)

    # print("PEOPLE IN ARR1 BUT NOT IN ARR2")
    # for j in arr1:
    #     if j not in arr2:
    #         print(j)
    # print("PEOPLE IN ARR2 BUT NOT IN ARR1")
    # for j in arr2:
    #     if j not in arr1:
    #         print(j)

copy_of_shapes = copy.deepcopy(Pentominoe.existingshapes)

Pentominoe.existingshapes = []

print(pentC.get_shapes(pentA))
print(pentA.get_shapes(pentC))
# print(len(pentA.existingshapes))

iterator = copy.deepcopy(Pentominoe.existingshapes)
Pentominoe.existingshapes = copy.deepcopy(copy_of_shapes)

for i, shape in enumerate(iterator):
    print(shape)
    pentominoe = Pentominoe("V", shape=shape)
    print(i, pentominoe.get_shapes(pentB))
    print(i, pentB.get_shapes(pentominoe))

for i in Pentominoe.existingshapes:
    if i not in copy_of_shapes:
        print(i)

print(f"the count is {len(Pentominoe.existingshapes)}")
# import pandas as pd
# # sample_list = [1,2,3,4,3,5,3,6,7,8]
# unique_list = list(pd.Series(Pentominoe.existingshapes).drop_duplicates())
#
# print(len(unique_list))

# 1123


# for i in pentA.existingshapes:
#     print(repr(i))

"""
1:34:55 2a complete
"""
