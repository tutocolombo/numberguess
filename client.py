import checker
import numfunc
import bot


if __name__ == "__main__":
    number = list(numfunc.get_num())
    finished = 0
    mode = input("Would you like to play (enter 0 or 1):\n [0] alone\n [1] against a computer\n")
    if mode:
        the_bot = bot.Bot()
        code = input("Playing against a computer.\nYour secret number? ")
        the_bot.number = numfunc.conv_num(code)
        print("You go first")
    print("Guess a 4 digit number. Any non-numeric character or blank space will be replaced with 0 (zero)")
    while not finished:
        guess = input("Your guess? ")
        result = checker.check(numfunc.conv_num(guess), number.copy())
        if not result:
            print("Correct")
            finished = 1
        else:
            print("{} -> {}M{}C".format(''.join(numfunc.conv_num(guess)), result[0], result[1]))
            if mode:
                finished = not the_bot.play()
    print("Game Over")