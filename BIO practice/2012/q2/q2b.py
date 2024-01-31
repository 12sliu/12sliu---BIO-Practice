from lib_trains import RailwayManager

test = RailwayManager("", "PV")
test.init_train("PV", "AB")

def func():
    test.update_train1(1)
    if test.train1.point:
        print(test.train1.curedge.point1.charrepr + test.train1.curedge.point2.charrepr)
    else:
        print(test.train1.curedge.point2.charrepr + test.train1.curedge.point1.charrepr)

func()
while test.train1.curedge.point1.charrepr != "P":
    func()
