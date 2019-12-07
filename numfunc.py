import random


def get_num():
    rn = random.randint(0, 9999)
    return "{:004d}".format(rn)


def replace(c):
    if not c.isdigit():
        c = '0'
    return c


def conv_num(n, d=4):
    n = list(map(replace, list(n)))
    while len(n) < d:
        n.insert(0, '0')
    return n[:4]
