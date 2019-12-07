import checker
import numfunc
import random


class Bot:
    def __init__(self):
        self.codes = list(range(0, 10000))
        self.finished = 0
        self.turn = 0
        self.guess = 1122
        self.number = []

    def play(self):
        self.codes.remove(self.guess)
        result = checker.check(list("{:004d}".format(self.guess)), self.number.copy())
        if not result:
            print("Bot turn: {}. {:004d} -> correct!".format(self.turn, self.guess))
            return 0
        print("Bot turn: {}. {:004d} -> {}M{}C".format(self.turn, self.guess, result[0], result[1]))
        self.codes = [x for x in self.codes if result == checker.check(list("{:004d}".format(x)), list("{:004d}".format(self.guess)))]
        self.turn += 1
        self.guess = random.choice(self.codes)
        return 1


if __name__ == "__main__":
    bot = Bot()
    number = input("Your secret number? ")
    bot.number = numfunc.conv_num(number)
    while bot.play():
        continue

