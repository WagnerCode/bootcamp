import copy

class Vector:
    flag = None
    shape = None
    def __init__(self, vector):
        if isinstance(vector, list):
            if len(vector) > 1:
                self.flag = 1
                self.vector = vector
                self.shape = (len(vector), 1)
            elif len(vector) == 1:
                self.flag = 2
                self.vector = vector
                self.shape = (1, len(vector[0]))
            else:
                print("ERROR")
        elif isinstance(vector, int):
            output = []
            for i in range(0, vector):
                help = []
                help.append(float(i))
                output.append(help)
            self.vector = copy.deepcopy(output)
            self.shape = (len(self.vector), 1)
            self.flag = 1
        elif isinstance(vector, tuple):
            output = []
            for i in range(vector[0], vector[1]):
                help = []
                help.append(float(i))
                output.append(help)
            self.vector = copy.deepcopy(output)
            self.shape = (len(self.vector), 1)
            self.flag = 1
        else:
            print("ERROR")


    def __mul__(self, other):
        i = 0
        output = copy.deepcopy(self.vector)
        if self.flag == 1:
            for item in self.vector:
                output[i][0] = item[0] * other
                i += 1
        elif self.flag == 2:
            i = 0
            for i in range(len(self.vector[0])):
                output[0][i] *= other

        return output

    def __rmul__(self, other):
        i = 0
        output = copy.deepcopy(self.vector)
        if self.flag == 1:
            for item in self.vector:
                output[i][0] = item[0] * other
                i += 1
        elif self.flag == 2:
            i = 0
            for i in range(len(self.vector[0])):
                output[0][i] *= other

        return output

    def __truediv__(self, other):
        i = 0
        output = copy.deepcopy(self.vector)
        if self.flag == 1:
            for item in self.vector:
                output[i][0] = item[0] / other
                i += 1
        elif self.flag == 2:
            i = 0
            for i in range(len(self.vector[0])):
                output[0][i] /= other

        return output

    def __rtruediv__(self, other):
        print("ERROR division of a scalar by a Vector")

    def __add__(self, other):
        i = 0
        output = copy.deepcopy(self.vector)
        if self.flag == 1:
            for item in self.vector:
                output[i][0] = item[0] + other.vector[i][0]
                i += 1
        elif self.flag == 2:
            i = 0
            for i in range(len(self.vector[0])):
                output[0][i] += other.vector[0][i]

        return output

    def __radd__(self, other):
        i = 0
        output = copy.deepcopy(self.vector)
        if self.flag == 1:
            for item in self.vector:
                output[i][0] = item[0] + other.vector[i][0]
                i += 1
        elif self.flag == 2:
            i = 0
            for i in range(len(self.vector[0])):
                output[0][i] += other.vector[0][i]

        return output

    def __sub__(self, other):
        i = 0
        output = copy.deepcopy(self.vector)
        if self.flag == 1:
            for item in self.vector:
                output[i][0] = item[0] - other.vector[i][0]
                i += 1
        elif self.flag == 2:
            i = 0
            for i in range(len(self.vector[0])):
                output[0][i] -= other.vector[0][i]

        return output

    def __rsub__(self, other):
        i = 0
        output = copy.deepcopy(self.vector)
        if self.flag == 1:
            for item in self.vector:
                output[i][0] = item[0] - other.vector[i][0]
                i += 1
        elif self.flag == 2:
            i = 0
            for i in range(len(self.vector[0])):
                output[0][i] -= other.vector[0][i]

        return output

    def __str__(self):
        return str(self.vector)
    def __repr__(self):
        pass

    def dot(self, other):
        i = 0
        HAHAHA = 0
        if self.shape != other.shape:
            HAHAHA = "ERROR ERROR"
        else:
            if self.flag == 1:
                for item in self.vector:
                    self.vector[i][0] = item[0] * other.vector[i][0]
                    HAHAHA += self.vector[i][0]
                    i += 1

            elif self.flag == 2:
                for item in self.vector[0]:
                    self.vector[0][i] = item * other.vector[0][i]
                    HAHAHA += self.vector[0][i]
                    i += 1

            elif self.flag == 2:
                i = 0
                for i in range(len(self.vector[0])):
                    self.vector[0][i] *= other.vector[0][i]
                HAHAHA = self.vector
        return HAHAHA

    def T(self):
        i = 1
        output = [[]]

        if self.flag == 1:
            for item in self.vector:
                output[0].append(item[0])
            self.vector = copy.deepcopy(output)
            self.shape = (1, len(self.vector))
        elif self.flag == 2:
            output = []
            for item in self.vector[0]:
                help = []
                help.append(item)
                output.append(help)
            self.vector = copy.deepcopy(output)
            self.shape = (len(self.vector), 1)
        return self.vector

v3 = Vector([[0.0], [1.0], [2.0], [3.0]])
v3_3 = Vector([[0.0], [1.0], [2.0], [3.0]])
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v1_1 = Vector([[0.0, 1.0, 2.0, 3.0]])

v228 = Vector(3)
v229 = Vector(3)

v230 = Vector((10, 16))

print(v1.dot(v1_1))
print(v3.dot(v3_3))



print(v230)


