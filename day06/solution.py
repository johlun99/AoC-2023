with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

def mult(w):
    ans = 1
    for n in w:
        ans *= n

    return ans

acc = 1
ways_to_win = []

for p in range(0, 2):
    if p == 0:
        times = [int(i) for i in lines[0].split(": ")[1].split(" ") if i.isdigit()]
        dist = [int(i) for i in lines[1].split(": ")[1].split(" ") if i.isdigit()]
    
    else:
        times = ""
        dist = ""

        numbers = [i for i in lines[0].split(": ")[1]]
        for n in numbers:
            if n.isdigit():
                times += n

        numbers = [i for i in lines[1].split(": ")[1]]
        for n in numbers:
            if n.isdigit():
                dist += n

        times = [int(times)]
        dist = [int(dist)]

    ways_to_win = []
    for i, t in enumerate(times):
        do_continue = True

        wins = []
        for h in range(0, t):
            tt = t-h
            d = tt * h

            if d > dist[i]:
                do_continue = False
                wins.append(h)

            elif do_continue == False:
                break

        ways_to_win.append(len(wins))

    print("Part: " + str(p + 1) + ": " + str(mult(ways_to_win)))
