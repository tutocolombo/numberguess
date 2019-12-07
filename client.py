import checker
import numfunc


if __name__ == "__main__":
    number = list(numfunc.get_num())
    finished = 0
    print("Guess a 4 digit number. Any non-numeric character or blank space will be replaced with 0 (zero)")
    while not finished:
        guess = input("Your guess? ")
        result = checker.check(numfunc.conv_num(guess), number.copy())
        if not result:
            print("Correct")
            finished = 1
        else:
            print("{} -> {}M{}C".format(''.join(numfunc.conv_num(guess)), result[0], result[1]))
