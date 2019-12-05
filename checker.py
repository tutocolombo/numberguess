import sys


def check(n1, n2):
    if n1 == n2:
        return 0
    good = 0
    reg = 0
    for i in range(len(n1)):
        if n1[i] == n2[i]:
            good += 1
            n1[i] = "n1"
            n2[i] = "n2"
    for j in range(len(n1)):
        for k in range(len(n2)):
            if n1[j] == n2[k]:
                reg += 1
                n1[j] = "n1"
                n2[k] = "n2"
                break
    return good, reg


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("need 2 numbers")
    if len(sys.argv[1]) != len(sys.argv[2]):
        sys.exit("need same length numbers")

    print(check(list(sys.argv[1]), list(sys.argv[2])))

