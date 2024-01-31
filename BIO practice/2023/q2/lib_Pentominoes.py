import copy

shapes = {
    "F":[
        [0, 1, 1],
        [1, 1],
        [0, 1]
    ],
    "G":[
        [1, 1],
        [0, 1, 1],
        [0, 1]
    ],
    "I":[
        [1],
        [1],
        [1],
        [1],
        [1]
    ],
    "L": [
        [1],
        [1],
        [1],
        [1, 1]
    ],
    "J": [
        [0, 1],
        [0, 1],
        [0, 1],
        [1, 1]
    ],
    "N": [
        [0, 1],
        [1, 1],
        [1],
        [1]
    ],
    "M": [
        [1],
        [1, 1],
        [0, 1],
        [0, 1]
    ],
    "P": [
        [1, 1],
        [1, 1],
        [1]
    ],
    "Q": [
        [1, 1],
        [1, 1],
        [0, 1]
    ],
    "T": [
        [1, 1, 1],
        [0, 1],
        [0, 1]
    ],
    "U": [
        [1, 0, 1],
        [1, 1, 1]
    ],
    "V": [
        [1],
        [1],
        [1, 1, 1]
    ],
    "W": [
        [1],
        [1, 1],
        [0, 1, 1]
    ],
    "X": [
        [0, 1],
        [1, 1, 1],
        [0, 1]
    ],
    "Z": [
        [1, 1],
        [0, 1],
        [0, 1, 1]
    ],
    "S": [
        [0, 1, 1],
        [0, 1],
        [1, 1]
    ],
    "Y": [
        [0, 1],
        [1, 1],
        [0, 1],
        [0, 1]
    ],
    "A": [
        [1, 0],
        [1, 1],
        [1, 0],
        [1, 0]
    ]
}


class Pentominoe:
    shape = []
    toprows = 0
    leftcolumns = 0

    existingshapes = []

    def __init__(self, letter):
        self.shape = shapes[letter]

    def generate_points(self):
        arr = []

        for i, point in enumerate(self.shape[0]):
            if point == 1:
                arr.append([-1, i])
        for i, point in enumerate(self.shape[-1]):
            if point == 1:
                arr.append([len(self.shape), i])

        for i, line in enumerate(self.shape):
            if line[0] != 0:
                arr.append([i, -1])
            for j, point in enumerate(line):
                if point == 0:
                    arr.append([i, j])
            arr.append([i, len(line)])

        return arr

    def transpose(self, pent1_point, pent2_point, pent2shape):

        activeshape = copy.deepcopy(pent2shape)
        for i, line in enumerate(self.shape):
            for j, point in enumerate(line):
                if point == 1:
                    newpos = [i-pent1_point[0] + pent2_point[0], j-pent1_point[1] + pent2_point[1]]
                    if newpos[0] < 0 or newpos[0] > len(pent2shape) - 1:
                        pass
                    elif newpos[1] < 0 or newpos[1] > len(pent2shape[newpos[0]]) - 1:
                        pass
                    elif pent2shape[newpos[0]][newpos[1]] == 1:
                        return False
                    activeshape = self.addtoshape(activeshape, newpos)
        # tuple_activeshape = (tuple(line) for line in activeshape)
        # print(activeshape)
        if activeshape not in self.existingshapes:
            self.existingshapes.append(activeshape)
            return True
        else:
            return False

    def addtoshape(self, activeshape, newpos):
        newpos[0] += self.toprows
        newpos[1] += self.leftcolumns

        # print(activeshape)

        while newpos[0] < 0:
            self.toprows += 1
            activeshape.insert(0, [])
            newpos[0] += 1
        while newpos[0] > len(activeshape) - 1:
            activeshape.append([])

        while newpos[1] < 0:
            self.leftcolumns += 1
            for line in activeshape:
                line.insert(0, 0)
            newpos[1] += 1
        while newpos[1] > len(activeshape[newpos[0]]) - 1:
            activeshape[newpos[0]].append(0)

        # print(newpos[0], newpos[1], len(activeshape), len(activeshape[newpos[0]]))
        activeshape[newpos[0]][newpos[1]] = 1
        for i, line in enumerate(activeshape):
            if len(line) > 0:
                if line[-1] == 0:
                    line.pop(-1)
        return activeshape

    def get_shapes(self, pent2):
        points = pent2.generate_points()
        count = 0

        for pent2_point in points:
            for i, line in enumerate(self.shape):
                for j, pent1_point in enumerate(line):
                    # print(i, j)
                    # print(line)
                    if pent1_point == 1:
                        # print(pent2.shape)
                        if self.transpose([i, j], pent2_point, pent2.shape):
                            count += 1
                    self.toprows = 0
                    self.leftcolumns = 0
        return count

    @staticmethod
    def check_if_internal_hole(shape):
        longest_line = 0
        for line in shape:
            longest_line = len(line) if len(line) > longest_line else longest_line
        for i, line in enumerate(shape):
            if i == 0 or i == len(shape) -1:
                continue
            for j, point in enumerate(line):
                if Pentominoe.sus_hole(shape, [i, j]):
                    # print(i, j, shape)
                    # sleep(10000)
                    return True

    @staticmethod
    def sus_hole(shape, hole, wasrecursive=None):
        i, j = hole
        line = shape[i]
        if shape[i][j] == 0:
            newshape = copy.deepcopy(shape)
            newshape[i][j] = 1
            if len(shape[i - 1]) <= j or len(shape[i + 1]) <= j or len(line)-1 <= j or 1 > j:
                return False
            if shape[i - 1][j] != 1:
                if i-1 != 0 and i-1 != len(shape)-1:
                    if Pentominoe.sus_hole(newshape, [i-1, j], wasrecursive=shape):
                        pass
                    else:
                        return False
                else:
                    return False
            if shape[i + 1][j] != 1:
                if i + 1 != 0 and i + 1 != len(shape) - 1:
                    if Pentominoe.sus_hole(newshape, [i+1, j], wasrecursive=shape):
                        pass
                    else:
                        return False
                else:
                    return False
            if line[j - 1] != 1:
                if Pentominoe.sus_hole(newshape, [i, j-1], wasrecursive=shape):
                    pass
                else:
                    return False
            if line[j + 1] != 1:
                if Pentominoe.sus_hole(newshape, [i, j+1], wasrecursive=shape):
                    pass
                else:
                    return False
            # if wasrecursive is not None:
            #     print(wasrecursive)
            return True
