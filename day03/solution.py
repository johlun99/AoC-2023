with open("input.txt", "r") as f:
    lines = f.read().splitlines()

p2_total = 0
cs = set()

for p in range(0, 2):
    for r, row in enumerate(lines):
        for c, ch in enumerate(row):
            if p == 0 and ch.isdigit() or ch == '.':
                continue

            if p == 1 and ch != "*":
                continue

            if p == 0:
                for dr in range(r - 1, r + 2 if p == 0 else r + 1):
                    for dc in range(c - 1, c + 2 if p == 0 else r + 1):
                        if dr < 0 or dr >= len(lines) or dc < 0 or dc >= len(lines[dr]) or not lines[dr][dc].isdigit():
                            continue

                        while dc > 0 and lines[dr][dc - 1].isdigit():
                            dc -= 1

                        cs.add((dr, dc))

            if p == 1:
                cs = set()

                for cr in [r - 1, r, r + 1]:
                    for cc in [c - 1, c, c + 1]:
                        if cr < 0 or cr >= len(lines) or cc < 0 or cc >= len(lines[cr]) or not lines[cr][cc].isdigit():
                            continue

                        while cc > 0 and lines[cr][cc - 1].isdigit():
                            cc -= 1

                        cs.add((cr, cc))

                if len(cs) != 2:
                    continue

                nums = []

                for cr, cc in cs:
                    num = ""
                    while cc < len(lines[cr]) and lines[cr][cc].isdigit():
                        num += lines[cr][cc]
                        cc += 1

                    nums.append(int(num))

                p2_total += nums[0] * nums[1]

validNums = []

for r, c in cs:
    num = ""
    while c < len(lines[r]) and lines[r][c].isdigit():
        num += lines[r][c]
        c += 1

    validNums.append(int(num))

print("Part 1: " + str(sum(validNums)))
print("Part 2: " + str(p2_total))
