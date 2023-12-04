from collections import defaultdict

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]


cards = {}
scores = tuple()

tickets = defaultdict(lambda: 0)

for i, l in enumerate(lines):
    tickets[i] += 1
    _id, val = l.split(": ")
    v0, v1 = val.split(" | ")
    winners = [int(i) for i in v0.split(" ") if len(i) > 0]
    checkers = [int(i) for i in v1.split(" ") if len(i) > 0]

    n = len([i for i in checkers if i in winners])

    if n == 0:
        continue

    scores += (2**(n-1),)

    for j in range(n):
        tickets[i+1+j] += tickets[i]


print("Part1: " + str(sum(scores)))
print("Part2: " + str(sum(tickets.values())))
