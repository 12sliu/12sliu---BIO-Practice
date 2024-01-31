from lib_Pentominoes import Pentominoe, shapes

target = input()

pentA = Pentominoe(target[0])
pentB = Pentominoe(target[1])
#
print(pentA.get_shapes(pentB))
for i in pentA.existingshapes:
    print(i)
# for i in pentA.existingshapes:
#     print(repr(i))

"""
1:34:55 2a complete
"""
