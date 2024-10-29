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
    lol = ""
    gog = ""
    for i in range(0, len(iterable) - 1, 2):
         gog += function_to_apply(iterable[i], iterable[i+1])
    if len(gog) != len(iterable):
        gog += iterable[len(iterable) - 1]
    yield gog






x = [1, 2, 3, 4, 5]

(ft_map(lambda dum: dum + 1, x))

print(list(ft_filter(lambda dum: not (dum % 2), x)))

lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']

print(list(ft_reduce(lambda u, v: u + v, lst)))

dd = lambda u, v: u + v

print(dd("5", "5"))