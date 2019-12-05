import sys

if len(sys.argv) != 3:
    sys.exit("need 2 numbers")
if len(sys.argv[1]) != len(sys.argv[2]):
    sys.exit("need same length numbers")
n1 = list(sys.argv[1])
n2 = list(sys.argv[2])
if n1 == n2:
    print("correct")
    sys.exit(0)
good = 0
reg = 0

for i in range(len(n1)):
    if n1[i] == n2[i]:
        good += 1
        n1[i] = "n1"
        n2[i] = "n2"
for j in n1:
    for k in n2:
        if k == j:
            reg += 1
            break

print(str(good) + "G " + str(reg) + "R")
sys.exit(0)
