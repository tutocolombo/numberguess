import checker
import numfunc
import bot
import socket


def client():
    host, port = [input("Enter game host: "), int(input("And port: "))]
    s = socket.socket()
    while True:
        try:
            s.connect((host, port))
        except Exception as e:
            print("something's wrong with {}:{}. Exception is {}".format(host, port, e))
            host, port = [input("Enter game host: "), int(input("And port: "))]
        else:
            print("Connection established")
            break

    my_code = input("Pick yout secret number: ")
    my_code = numfunc.conv_num(my_code)
    while True:
        go_token = s.recv(1024).decode('utf-8')
        print(go_token)
        my_guess = input("Your guess? ")
        my_guess = ''.join(numfunc.conv_num(my_guess))
        s.send(my_guess.encode('utf-8'))
        my_result = s.recv(1024).decode('utf-8')
        if not my_result:
            print("Correct")
            break
        print("{} -> {}M{}C".format(my_guess, my_result[0], my_result[1]))
        s.send("Your turn".encode('utf-8'))
        their_guess = s.recv(1024).decode('utf-8')
        print("Their guess: {}".format(their_guess))
        their_result = checker.check(numfunc.conv_num(their_guess), my_code.copy())
        if not their_result:
            print("You loose")
            break
        s.send(''.join(their_result).encode('utf-8'))
    s.close()


def server():
    host = socket.gethostname()
    port = 8080

    s = socket.socket()
    s.bind((host, port))

    print("Game created in host: {} port: {}".format(host, port))
    s.listen(1)
    client_s, addr = s.accept()
    print("{} joined the game.".format(addr))

    my_code = input("Pick yout secret number: ")
    my_code = numfunc.conv_num(my_code)
    client_s.send("Guests go first".encode('utf-8'))
    while True:
        their_guess = client_s.recv(1024).decode('utf-8')
        print("Their guess: {}".format(their_guess))
        their_result = checker.check(numfunc.conv_num(their_guess), my_code.copy())
        if not their_result:
            print("You loose")
            break
        client_s.send(''.join(their_result).encode('utf-8'))
        go_token = client_s.recv(1024).decode('utf-8')
        print(go_token)
        my_guess = input("Your guess? ")
        my_guess = ''.join(numfunc.conv_num(my_guess))
        client_s.send(my_guess.encode('utf-8'))
        my_result = client_s.recv(1024).decode('utf-8')
        if not my_result:
            print("Correct")
            break
        print("{} -> {}M{}C".format(my_guess, my_result[0], my_result[1]))
        client_s.send("Your turn".encode('utf-8'))

    client_s.close()
    s.close()


if __name__ == "__main__":
    number = list(numfunc.get_num())
    finished = 0
    mode = input("Would you like to play\n [0] alone\n [1] against a computer\n [2] host a multiplayer game\n [3] join a multiplayer game\n")
    if mode == '2':
        server()
    if mode == '3':
        client()
    if mode == '1':
        the_bot = bot.Bot()
        code = input("Playing against a computer.\nYour secret number? ")
        the_bot.number = numfunc.conv_num(code)
        print("You go first")
    if (mode == '0') | (mode == '1'):
        print("Guess a 4 digit number. Any non-numeric character or blank space will be replaced with 0 (zero)")
        while not finished:
            guess = input("Your guess? ")
            result = checker.check(numfunc.conv_num(guess), number.copy())
            if not result:
                print("Correct")
                finished = 1
            else:
                print("{} -> {}M{}C".format(''.join(numfunc.conv_num(guess)), result[0], result[1]))
                if mode == 1:
                    finished = not the_bot.play()
    print("Game Over")
