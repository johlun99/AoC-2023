with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

part1 = 0
part2 = 0

for line in lines:
    p1_digits = []
    p2_digits = []

    for i, c in enumerate(line):
        if c.isdigit():
            p1_digits.append(c)
            p2_digits.append(c)

            continue

        for index, text_num in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(text_num):
                p2_digits.append(str(index + 1))

    part1 += int(p1_digits[0] + p1_digits[-1])
    part2 += int(p2_digits[0] + p2_digits[-1])

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
