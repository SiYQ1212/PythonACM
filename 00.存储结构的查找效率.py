import time


def cal(func):
    def inner(*args):
        t1 = time.time()
        res = func(*args)
        t2 = time.time()
        print(f"{func.__name__} speed {t2 -t1:.8f} s")
        return res
    return inner


@cal
def listspeed(org):
    n = 0
    ls = list(org)
    for i in org:
        if i in ls:
            n += 1


@cal
def tuplespeed(org):
    n = 0
    tp = tuple(org)
    for i in org:
        if i in org:
            n += 1


@cal
def setspeed(org):
    n = 0
    se = set(org)
    for i in org:
        if i in se:
            n += 1


@cal
def dictspeed(org):
    n = 0
    dc = dict()
    for i in org:
        dc[i] = 0
    for i in org:
        if dc.get(i):
            n += 1


if __name__ == '__main__':
    org = [i for i in range(2, 50000, 2)]
    listspeed(org)
    tuplespeed(org)
    setspeed(org)
    dictspeed(org)
    # The rank of the run rate is Set > Dict >> Tuple = List
