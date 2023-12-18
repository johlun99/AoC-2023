import sys

with open(sys.argv[1], "r") as f:
    l = [l.strip() for l in f.readlines()][0]

steps = l.split(",")
print(steps)

total = 0
for s in steps:
    CV = 0
    for c in s:
        CV += ord(c)
        CV *= 17
        CV %= 256

        print(CV)

    total += CV

print("Part 1: " + str(total))
