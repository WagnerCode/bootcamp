import math

class TinyStatistician:
    def mean(self, x):
        result = 0
        m = len(x)
        for number in x:
            result += number

        return result / m

    def median(self, x):
        x.sort()
        case = len(x)

        if case % 2 != 0:
            i = (case + 1) / 2
            return float(x[int(i) - 1])
        else:
            return (case / 2) + ((case / 2) + 1) / 2

    def quartiles(self, x):
        x.sort()
        m = len(x)

        q1 = ((m + 1 )/ 4)
        q3 = ((m + 1) * 3 ) / 4
        return x[int(q1)], x[int(q3 - 1)]

    def var(self, x):
        resul = 0
        m = len(x)
        for number in x:
            resul += (number - self.mean(x))**2
        return resul / m
    def std(self, x):
        return math.sqrt(self.var(x))



tstat = TinyStatistician()

a = [1, 42, 300, 10, 59]

tstat.mean(a)

tstat.median(a)

tstat.quartiles(a)

tstat.var(a)

tstat.std(a)