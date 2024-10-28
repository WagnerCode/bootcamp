def myfunc(a):
    return len(a)
def myfunc2(a):
    return  a + 1

def ft_map(function_to_apply, iterable):
    for item in iterable:
        yield function_to_apply(item)

def ft_filter(function_to_apply, iterable):
    for item in iterable:
        if function_to_apply(item):
            yield item

def ft_reduce(function_to_apply, iterable):

    for i in range(len(iterable)):
        pass



x = [1, 2, 3, 4, 5]

(ft_map(lambda dum: dum + 1, x))

print(list(ft_filter(lambda dum: not (dum % 2), x)))

lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

print(list(ft_reduce(lambda u, v: u + v, lst)))


