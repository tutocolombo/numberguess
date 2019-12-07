import checker
import numfunc
import random


if __name__ == "__main__":
    codes = list(range(0, 10000))
    finished = 0
    turn = 0
    guess = 1122
    number = input("Your secret number? ")
    number = numfunc.conv_num(number)
    while not finished:
        codes.remove(guess)
        result = checker.check(list("{:004d}".format(guess)), number.copy())
        if not result:
            print("{:004d} is correct!".format(guess))
            finished = 1
            break
        print("Turn: {}. {:004d} -> {}M{}C".format(turn, guess, result[0], result[1]))
        codes = [x for x in codes if result == checker.check(list("{:004d}".format(x)), list("{:004d}".format(guess)))]
        turn += 1
        guess = random.choice(codes)
