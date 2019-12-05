import sys
import random
import checker


def get_num():
    rn = random.randint(0,9999)
    return "{:004d}".format(rn)


while 1:
    print(get_num())

