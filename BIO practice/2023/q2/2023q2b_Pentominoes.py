from lib_Pentominoes import Pentominoe, shapes


# target = input()

pentA = Pentominoe("W")
pentB = Pentominoe("X")
#
pentA.get_shapes(pentB)
XWshapes = pentA.existingshapes
print(len(pentA.existingshapes), len(XWshapes))

for i in shapes:
    for j in shapes:
        # print(i, j)
        value = True if i != "W" and j != "X" else False
        if i == "X" and j == "W":
            value = False
        if value:
            pentC = Pentominoe(i)
            pentD = Pentominoe(j)

            pentC.get_shapes(pentD)
            newshapes = pentC.existingshapes

            tempshapes = copy.deepcopy(XWshapes)

            for shape in XWshapes:
                # print("it works")
                if shape in newshapes:
                    # print("things not removed")
                    # print(len(tempshapes))
                    # print("something has been removed")
                    tempshapes.remove(shape)
                    # print(len(tempshapes))
            # print(tempshapes)
            XWshapes = copy.deepcopy(tempshapes)
        else:
            print(i, j)

print(len(pentA.existingshapes), len(XWshapes))

print(len(pentA.existingshapes) - len(XWshapes))

# for i in pentA.existingshapes:
#     print(repr(i))

"""
1:34:55 2a complete
1:50(?):00 2b looked at ans
2:03:42 stuck on 2b, took break
2:07:15 2b solved (with looking at ans)
2:12(?):00 2c programmed
2:17:00 lunch break
2:30(?):00 2c determined broken
2:17:00 2c fixed
2:25:00 2d done

final time 2:25:53
2A: 23/23
2B: 0/2
2C: 0/5
2D: 0/4
"""
