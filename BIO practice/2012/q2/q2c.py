import copy
from itertools import permutations, combinations, combinations_with_replacement, product
from lib_trains import RailwayManager, halfCurvedEdges, fullCurvedEdges, straightEdges

test = RailwayManager("")

allEdges = halfCurvedEdges + fullCurvedEdges + straightEdges
print(len(allEdges))
print(sum(1 for ignore in product(allEdges, repeat=2)))

for i in allEdges:
    print(i)
    count = 0
    for j in allEdges:
        if i != j:
            test.init_train(i[0] + i[1], j[0] + j[1])
            isGood = True
            for k in range(100):
                test.update_train1(1)
                test.update_train2(1)
                temp2 = test.train2.curedge.point2 if test.train2.point else test.train2.curedge.point1
                temp1 = test.train1.curedge.point2 if test.train1.point else test.train1.curedge.point1
                if test.train1.curedge == test.train2.curedge:
                    isGood = False
                    break
            if isGood:
                count += 1

print(count)

# if __name__ == '__main__':
#     # start 4 worker processes
#     with Pool(processes=4) as pool:
#         what = copy.deepcopy(allEdges)
#         # print "[0, 1, 4,..., 81]"
#         print(sum(pool.map(get_ans, what)))

# def func():
#     test.update_train1(1)
#     if test.train1.point:
#         print(test.train1.curedge.point1.charrepr + test.train1.curedge.point2.charrepr)
#     else:
#         print(test.train1.curedge.point2.charrepr + test.train1.curedge.point1.charrepr)
#
# func()
# while test.train1.curedge.point1.charrepr != "P":
#     func()
