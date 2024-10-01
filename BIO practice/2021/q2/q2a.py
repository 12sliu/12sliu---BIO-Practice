class Hexagon:
    def __init__(self, num):
        self.edgeDict = {}
        self.num = num

    def get_color(self, mod):
        counter = 0 + mod
        for i in self.edgeDict:
            if i.color == "b":
                counter -= 1
            elif i.color == "r":
                counter += 1
        if counter == 0:
            return ""
        elif counter > 0:
            return "r"
        else:
            return "b"




class Edge:
    def __init__(self):
        self.color = ""
        self.hexagons = []

    def __repr__(self):
        return f"{[thing.num for thing in self.hexagons]}"

    def lowest_hex(self):
        return self.hexagons[0] if self.hexagons[0].num < self.hexagons[1] else self.hexagons[1]

    def highest_hex(self):
        return self.hexagons[0] if self.hexagons[0].num > self.hexagons[1] else self.hexagons[1]


def opposite_side(num):
    return num + 3 if num < 4 else num - 3

hexagonList = [Hexagon(i+1) for i in range(25)]

def check_other_hex(hexagon, addHexagon, oldedge, num):
    for correctEdge in addHexagon.edgeDict.keys():
        print(hexagon.num)
        print(oldedge)
        print(hexagon.edgeDict)
        print(addHexagon.num, addHexagon.edgeDict, sep="")
        if addHexagon.edgeDict[correctEdge] == opposite_side(num):
            hexagon.edgeDict.pop(oldedge)
            hexagon.edgeDict[correctEdge] = num
            print(hexagon.edgeDict)
            return
    addHexagon.edgeDict[oldedge] = (opposite_side(num))
    oldedge.hexagons.append(addHexagon)


for hexagon in hexagonList:
    edge1 = Edge()
    hexagon.edgeDict[edge1] = 6
    edge2 = Edge()
    hexagon.edgeDict[edge2] = 1
    edge1.hexagons.append(hexagon)
    edge2.hexagons.append(hexagon)
    if hexagon.num < 6:
        continue
    if not hexagon.num == 1 and not hexagon.num == 11:
        if int(str(hexagon.num)[-1]) > 5:
            addHexagon = hexagonList[hexagon.num - 1 - 5]
        else:
            addHexagon = hexagonList[hexagon.num - 1 - 6]
        check_other_hex(hexagon, addHexagon, edge1, 6)

    if not hexagon.num == 10 and not hexagon.num == 20:
        if int(str(hexagon.num)[-1]) > 5:
            addHexagon = hexagonList[hexagon.num - 1 - 4]
        else:
            addHexagon = hexagonList[hexagon.num - 1 - 5]
        check_other_hex(hexagon, addHexagon, edge2,1)

for hexagon in hexagonList:
    edge1 = Edge()
    hexagon.edgeDict[edge1] = 4
    edge2 = Edge()
    hexagon.edgeDict[edge2] = 3
    edge1.hexagons.append(hexagon)
    edge2.hexagons.append(hexagon)
    if hexagon.num > 20:
        continue
    if not hexagon.num == 1 and not hexagon.num == 11:
        if int(str(hexagon.num)[-1]) > 5:
            addHexagon = hexagonList[hexagon.num - 1 + 5]
        else:
            addHexagon = hexagonList[hexagon.num - 1 + 4]
        check_other_hex(hexagon, addHexagon, edge1, 4)

    if not hexagon.num == 10 and not hexagon.num == 20:
        if int(str(hexagon.num)[-1]) > 5:
            addHexagon = hexagonList[hexagon.num - 1 + 6]
        else:
            addHexagon = hexagonList[hexagon.num - 1 + 5]
        check_other_hex(hexagon, addHexagon, edge2, 3)

for hexagon in hexagonList:
    edge1 = Edge()
    hexagon.edgeDict[edge1] = 5
    edge2 = Edge()
    hexagon.edgeDict[edge2] = 2
    edge1.hexagons.append(hexagon)
    edge2.hexagons.append(hexagon)
    if (hexagon.num - 1) % 5 != 0:
        addHexagon = hexagonList[hexagon.num - 1 - 1]
        check_other_hex(hexagon, addHexagon,edge1, 5)
    if hexagon.num % 5 != 0:
        addHexagon = hexagonList[hexagon.num - 1 + 1]
        check_other_hex(hexagon, addHexagon,edge2, 2)

def skirmish(number, r, b):
    redDroneDirection = 1
    redDronePosition = 1
    blueDroneDirection = 6
    blueDronePosition = 25
    for i in range(number):
        # red
        for edge in hexagonList[redDronePosition -1].edgeDict:
            if hexagonList[redDronePosition -1].edgeDict[edge] == redDroneDirection:
                edge.color = "r"
        redDroneDirection = redDroneDirection + 1 if redDronePosition != 6 else 1
        redDronePosition = redDronePosition + r
        if redDronePosition > 25:
            redDronePosition -= 25

        # blue
        for edge in hexagonList[blueDronePosition -1].edgeDict:
            if hexagonList[redDronePosition -1].edgeDict[edge] == blueDroneDirection:
                edge.color = "b"
        blueDroneDirection = blueDroneDirection - 1 if blueDronePosition != 0 else 6
        blueDronePosition = blueDronePosition + r
        if blueDronePosition > 25:
            blueDronePosition -= 25

def _feud(color):

    otherColor = "b" if color == "r" else "r"

    optimalList = []
    for hexagon in hexagonList:
        for edge in hexagon.edgeDict:
            if edge == "r" or edge == "b":
                continue
            controlCounter = 0
            takeawayCounter = 0
            for connectedHexagon in edge.hexagons:
                if connectedHexagon.get_color(1) == color:
                    controlCounter += 1
                if connectedHexagon.get_color(0) == otherColor:
                    takeawayCounter += 1
            if optimalList[0][0] > controlCounter:
                continue
            elif optimalList[0][0] == controlCounter:
                if optimalList[0][1] > takeawayCounter:
                    continue
                elif optimalList[0][1] == takeawayCounter:
                    optimalList.append((controlCounter, takeawayCounter, edge, hexagon))
                else:
                    optimalList.clear()
                    optimalList.append((controlCounter, takeawayCounter, edge, hexagon))
            else:
                optimalList.clear()
                optimalList.append((controlCounter, takeawayCounter, edge, hexagon))
        if color == "b":
            optimalList = optimalList[::-1]
        optimalList[0]


def feud(number):
    for i in range(number):
        _feud("r")
        _feud("b")

for hexagon in hexagonList:
    print(hexagon.edgeDict)
    print(hexagon.get_color(0))

r, b = input().split()
s, f = input().split()

skirmish(s, r, b)
feud(f)

r_count = 0
b_count = 0

for hexagon in hexagonList:
    if hexagon.get_color(0) == "r":
        r_count += 1
    elif hexagon.get_color(0) == "b":
        b_count += 1

print(r_count)
print(b_count)
