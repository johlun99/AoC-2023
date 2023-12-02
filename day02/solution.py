with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def multiplyList(myList):
    result = 1
    for x in myList:
        result *= myList[x]

    return result


cubes_available = {
    "red": 12,
    "green": 13,
    "blue": 14
}

powers = []
impossible = []
possible_ids = []
for line in lines:
    possible = True
    cubes_current = []
    game, row = line.split(": ")
    sets = row.split("; ")
    min_required = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for s in sets:
        cube_set = s.split(", ")
        for cs in cube_set:
            num, color = cs.split(" ")
            num = int(num)
            cubes_current.append(int(num))

            if cubes_available[color] < num and game not in impossible:
                possible = False
                impossible.append(game)

            if min_required[color] == 0 or min_required[color] < num:
                min_required[color] = num

    powers.append(multiplyList(min_required))
    if possible:
        possible_ids.append(int(game.split(" ")[1]))

print("Part 1: " + str(sum(possible_ids)))
print("Part 2: " + str(sum(powers)))
