import copy
from typing import List

halfCurvedEdges = [
    ("E", "A"),
    ("F", "A"),
    ("G", "B"),
    ("H", "B"),
    ("I", "C"),
    ("J", "C"),
    ("K", "D"),
    ("L", "D"),
    ("M", "U"),
    ("N", "U"),
    ("O", "V"),
    ("P", "V"),
    ("Q", "W"),
    ("R", "W"),
    ("S", "X"),
    ("T", "X")
]

fullCurvedEdges = [
    ("M", "E"),
    ("N", "E"),
    ("N", "F"),
    ("O", "F"),
    ("O", "G"),
    ("P", "G"),
    ("P", "H"),
    ("Q", "H"),
    ("Q", "I"),
    ("R", "I"),
    ("R", "J"),
    ("S", "J"),
    ("S", "K"),
    ("T", "K"),
    ("T", "L"),
    ("M", "L")
]

straightEdges = [
    ("D", "A"),
    ("C", "B"),
    ("V", "U"),
    ("X", "W"),
]


class Edge:
    def __init__(self, point1, point2):
        self.point1 = point1  # Station
        self.point2 = point2  # Station

    def __eq__(self, other):
        return self.point1.charrepr == other.point1.charrepr and self.point2.charrepr == other.point2.charrepr  # change that to your needs

    def __str__(self):
        return f"Edge {self.point1.charrepr + self.point2.charrepr}"

class Station:
    def __init__(self, charrepr: str, flipflop: bool):
        self.charrepr = charrepr
        self.flipflop = flipflop
        self.curvededges = []
        self.straightedge = None
        self.setedge = 0

    def add_curved_edges(self, curvededges: List[Edge]):
        self.curvededges = self.curvededges + curvededges

    def add_straight_edge(self, straightedge: Edge):
        self.straightedge = straightedge

    def process_train(self, edge):
        if self.flipflop:
            if edge == self.straightedge:
                self.setedge = 1 - self.setedge
                return self.curvededges[1 - self.setedge]
            else:
                return self.straightedge
        else:
            # print("i is a lazy")
            # print(edge, self.straightedge, self.charrepr)
            if edge == self.straightedge:
#                 print("ENTERING FROM STRAIGHT, RETURNING CURVED")
                return self.curvededges[self.setedge]
            else:
#                 # print(self.curvededges)
                self.setedge = 0 if self.curvededges[0] == edge else 1
                return self.straightedge


class Train:
    curedge: Edge

    def __init__(self, edge: Edge, point: bool):
        self.curedge = edge
        self.point = point

    def get_station(self):
        if self.point:
            return self.curedge.point2
        return self.curedge.point1

    def set_edge(self, edge: Edge):
        oldedge = copy.deepcopy(self.curedge)
        self.curedge = edge
#         print("setting edge")
#         print(self.curedge)
        if self.curedge.point1.charrepr == oldedge.point1.charrepr or self.curedge.point1.charrepr == oldedge.point2.charrepr:
            self.point = True
        else:
            self.point = False
#         print(self.point)



class RailwayManager:

    stations = {}
    edges = {}

    def __init__(self, flipflops):

        for place in range(1, 25):

            flipflopbool = False
            letters = chr(place+64)
#             # print(letters)
            if letters in flipflops:
                flipflopbool = True
            self.stations[letters] = Station(letters, flipflopbool)
        temp = {}
        # halfcurved
        for i in halfCurvedEdges:
            self.edges[i[0] + i[1]] = (Edge(self.stations[i[0]], self.stations[i[1]]))
        for letters in self.edges:
            self.stations[letters[1]].add_curved_edges([self.edges[letters]])
            self.stations[letters[0]].add_straight_edge(self.edges[letters])
            # if letters[0] == "F":
#                 print(self.stations[letters[0]].straightedge, self.stations[letters[0]].curvededges, "FFF")
#         print(self.stations["F"].straightedge, self.stations["F"].curvededges, "FFF")
        temp = {}
        # fullcurved
        for i in fullCurvedEdges:
            self.edges[i[0] + i[1]] = (Edge(self.stations[i[0]], self.stations[i[1]]))
            temp[i[0] + i[1]] = (Edge(self.stations[i[0]], self.stations[i[1]]))
        for letters in temp:
            self.stations[letters[1]].add_curved_edges([self.edges[letters]])
            self.stations[letters[0]].add_curved_edges([self.edges[letters]])
#         print(self.stations["F"].straightedge, self.stations["F"].curvededges, "FFF")

        temp = {}
        # straight
        for i in straightEdges:
            self.edges[i[0] + i[1]] = (Edge(self.stations[i[0]], self.stations[i[1]]))
            temp[i[0] + i[1]] = (Edge(self.stations[i[0]], self.stations[i[1]]))
        for letters in temp:
            self.stations[letters[1]].add_straight_edge(self.edges[letters])
            self.stations[letters[0]].add_straight_edge(self.edges[letters])
#         print(self.stations["F"].straightedge, self.stations["F"].curvededges, "FFF")
#         # print(self.edges)
        self.train1 = None
        self.train2 = None

    def init_train(self, inp1, inp2):
        point1 = True
        point2 = True

        if inp1 not in self.edges:
            inp1 = inp1[::-1]
            point1 = not point1

        if inp2 not in self.edges:
            inp2 = inp2[::-1]
            point2 = not point2
        self.train1 = Train(self.edges[inp1], point1)
        self.train2 = Train(self.edges[inp2], point2)

    def update_train1(self, times):
        for i in range(times):
#             # print(self.train.get_station())
            station = self.train1.get_station()
#             print(f"station is {station.charrepr}", f"train last edge was {self.train.curedge}")
            edge = station.process_train(self.train1.curedge)
#             print(f"newest edge is {edge}")
            self.train1.set_edge(edge)

    def update_train2(self, times):
        for i in range(times):
#             # print(self.train.get_station())
            station = self.train2.get_station()
#             print(f"station is {station.charrepr}", f"train last edge was {self.train.curedge}")
            edge = station.process_train(self.train2.curedge)
#             print(f"newest edge is {edge}")
            self.train2.set_edge(edge)


# test = RailwayManager("GHIJKL", "AE")
# test.update(int(input()))

