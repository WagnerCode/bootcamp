class Evaluator:
    @staticmethod
    def zip_evaluate(b, a):
        baba = 0
        if len(b) != len(a):
            return print(-1)
        else:
            for i, j in zip(a, b):
                baba += len(i) * j
            print(baba)
    @staticmethod
    def enumerate_evaluate(a, b):
        baba = 0
        if len(b) != len(a):
            return print(-1)
        else:
            for i, j in enumerate(b):
                baba += a[i] * len(j)

        print(baba)
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]


Evaluator.zip_evaluate(coefs,words)
Evaluator.enumerate_evaluate(coefs,words)