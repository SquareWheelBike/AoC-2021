import sys

# AoC template for python3

# for now, only returns line points if the line is horizontal or vertical
def pointsInLine(line:list, diag=False):
    # print("\n",line[0], " -> ", line[1])
    # horizontal line
    if line[0][0] == line[1][0]:
        # print("horizontal")
        ran = sorted([line[0][1], line[1][1]])
        ran[1] += 1
        l = [(line[0][0], i) for i in range(*ran)]
    # vertical line
    elif line[0][1] == line[1][1]:
        # print("vertical")
        ran = sorted([line[0][0], line[1][0]])
        ran[1] += 1
        l = [(i, line[0][1]) for i in range(*ran)]
    # diagonal line
    elif diag == True: # this is hell
        ranx = sorted([line[0][0], line[1][0]]) # need to feed range smallest value first
        ranx[1] += 1                            # must increment upper bound
        ranx = list(range(*ranx))               # convert to list of range
        if (line[0][0] > line[1][0]):           # check if we need to reverse points; order is important for diagonals
            ranx.reverse()
        rany = sorted([line[0][1], line[1][1]]) # rinse and repeat
        rany[1] += 1
        rany = list(range(*rany))
        if (line[0][1] > line[1][1]):
            rany.reverse()
        l = [tuple(t) for t in list(zip(ranx, rany))]   # zip them together
    else:
        l = []
    # print(l)
    return l


def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    points = [[tuple([int(n) for n in t.strip().split(",")]) for t in l.split(" -> ")] for l in f] 

    # PART 1
    # each set of points is a line
    # store in a dict all the points, with an int count of how many lines they are on
    overlaps = {} # dictionary
    for p in points:
        for point in pointsInLine(p):
            if point in overlaps:
                overlaps[point] += 1
            else:
                overlaps[point] = 1
    # find the points that have more than one line on them
    gt2 = [k for k, v in overlaps.items() if v > 1]
    print("Part 1:", len(gt2))

    # PART 2
    # same thing, but with diagonals this time
    overlaps = {} # clear dictionary
    for p in points:
        for point in pointsInLine(p, True): # true just means do diagonals too
            if point in overlaps:
                overlaps[point] += 1
            else:
                overlaps[point] = 1
    # find the points that have more than one line on them
    gt2 = [k for k, v in overlaps.items() if v > 1]
    print("Part 2:", len(gt2))

if __name__ == "__main__":
    main()
