from lib_trains import RailwayManager

test = RailwayManager([x for x in input()])
test.init_train(input(), "VP")
test.update_train1(int(input()))
if test.train1.point:
    print(test.train1.curedge.point1.charrepr + test.train1.curedge.point2.charrepr)
else:
    print(test.train1.curedge.point2.charrepr + test.train1.curedge.point1.charrepr)