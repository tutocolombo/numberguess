import sys
import random
import checker


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
        n.append('0')
    return n[:4]


if __name__ == "__main__":
    number = list(get_num())
    finished = 0
    while not finished:
        guess = input("Your guess? ")
        result = checker.check(conv_num(guess), number.copy())
        if not result:
            print("Correct")
            finished = 1
        else:
            print("{}G{}R".format(result[0], result[1]))
