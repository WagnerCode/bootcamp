import numpy as np

class NumPyCreator:
    def from_list(self, lst):
        return np.array(lst)
    def from_tuple(self, tpl):
        return np.array(tpl)
    def from_iterable(self, itr):
        return np.fromiter(itr, float)
    def from_shape(self, shape, value=0):
        len = 1
        for i in shape:
            len *= i
        a = np.arange(len).reshape(shape)
        a.fill(value)

        return a

    def random(self, shape):
        rg = np.random.default_rng(1)
        a = rg.random(shape)
        return a
    def identity(self, n):
        return print(np.identity(n))


transformer = NumPyCreator()

a = [2, 3, 4]

transformer.from_list(a)
transformer.from_shape((2,3,3), 1)
transformer.random((2,3))
transformer.identity(4)