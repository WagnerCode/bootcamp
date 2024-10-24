import time
import sys
import copy

def ft_progress(lst):
    duma = len(lst) / 10
    duma_copy = copy.copy(duma)
    ravno = ''

    persent = len(lst) / 100 # 1 часть из 100 процентов
    persent_copy = copy.copy(persent)
    persent_view = 0

    start_time = time.time()
    ETA = 0
    for i in lst:

        end_time = time.time() - start_time
        if i == 1:
            storage = round(end_time, 2)
            ETA = storage * len(lst)
        rounded_time = round(end_time, 2)
        sys.stdout.write('ETA:%s [ %s] [%s>] %s/%s | elapsed time %ss\r' %(round(ETA - end_time, 2), persent_view, ravno, i, len(lst), rounded_time))
        sys.stdout.flush()
        if i == duma - 1:
            duma += duma_copy
            ravno += '='
        if i == persent:
            persent += persent_copy
            persent_view += 1
        yield i


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)