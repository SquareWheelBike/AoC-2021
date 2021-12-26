import sys
from itertools import product, count, permutations
from copy import deepcopy

def nextpos(pos, dir, r, c) -> tuple:
    x, y = pos
    if dir == '>':
        x = (x + 1) % c
    elif dir == 'v':
        y = (y + 1) % r
    else:
        print("ERROR: invalid direction", dir)
        exit(1)
    return (x, y)

def east(points:dict) -> set:
    return {(x, y) for (x, y) in points if points[(x, y)] == '>'}

def south(points:dict) -> set:
    return {(x, y) for (x, y) in points if points[(x, y)] == 'v'}

def printimage(points:dict, r:int, c:int):
    for y, x in product(range(r), range(c)):
        if (x, y) in points:
            print(points[(x, y)], end='')
        else:
            print('.', end='')
        if x == c - 1:
            print()
    print()

# points is a dict of (x,y) -> char, where char is either > or v
def part1(points:dict, r:int, c:int) -> int:
    # separate points into east and south herds
    # create an image of the points, where they stand now
    image = {}
    rounds = count()
    while image.keys() != points.keys():
        next(rounds)
        image = points  # copy previous image, no need for deepcopy
        eastpoints = {}
        for pos in east(image):
            newpos = nextpos(pos, '>', r, c)
            if newpos not in image: # east happens first, so look at all points in last round
                eastpoints[newpos] = '>'
            else:
                eastpoints[pos] = '>'
        southpoints = {}
        southimage = south(image)   # east have all changed, so look at southimage and eastpoints for conflicts
        for pos in southimage:
            newpos = nextpos(pos, 'v', r, c)
            if newpos not in southimage and newpos not in eastpoints:
                southpoints[newpos] = 'v'
            else:
                southpoints[pos] = 'v'
        points = eastpoints
        points.update(southpoints)
    return next(rounds)

# cannot do part 2 until all other puzzles are complete
def part2(points:dict) -> int:
    return 0

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]

    points = {}
    for y, l in enumerate(f):
        for x, ch in enumerate(l):
            if ch != '.':
                points[(x, y)] = ch
    r = len(f)
    c = len(f[0])

    print("Part 1:", part1(deepcopy(points), r, c))
    # print("Part 2:", part2(deepcopy(points)))


if __name__ == "__main__":
    main()