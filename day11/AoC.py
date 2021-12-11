import sys
from itertools import product, count
from copy import deepcopy

# AoC template for python3

# coord is y, x location tuple
# heightmap is a 2d list of ints
# returns list of points that are adjacent to the given coord
def adjacent(heightmap:list, coord:tuple) -> set:
    adjacent = set()
    y, x = coord
    # greatly reduced the number of points to check from big to <=9
    perm = product(range(max(0, y-1), min(y + 2, len(heightmap))), range(max(0, x-1), min(x + 2, len(heightmap[0]))))
    for i, j in perm:
        if y == i and x == j: # skip the current position
            continue
        adjacent.add((i, j))
    return adjacent

def part1(f:list) -> int:
    # octopi in a grid, each int is their energy level
    # for each day, increase the levels of each octopi by 1
    # if any octopi > 9, they truncate to 0 and 'flash'
    # any flashing octopus will also increase the level of all adjacent octopi by 1, not counting other flashing octopi
    flashes = 0 # we want to count the total number of flashes
    for day in range(0, 100):
        # for each octopus, increase their energy level by 1
        for y, x in product(range(len(f)), range(len(f[0]))):
            f[y][x] += 1

        # for each octopus, increment surrounding octopi by 1
        flashed = set() # keep track of which octopi flashed
        lastcycle = -1
        while len(flashed) != lastcycle:
            lastcycle = len(flashed)
            for y, x in product(range(len(f)), range(len(f[0]))):
                if (y,x) not in flashed and f[y][x] > 9:
                    # increase the energy level of all adjacent octopi by 1
                    flashed.add((y,x))
                    for i, j in adjacent(f, (y, x)):
                        f[i][j] += 1
        # reset flashed octopi to 0
        for y, x in flashed:
            f[y][x] = 0
        # keep track of total flashes
        flashes += len(flashed)

    return flashes

def part2(f:list) -> int:
    # find the first round where all octopi flash at once
    rounds = count()
    nfish = sum([len(l) for l in f])
    while True:
        # for each octopus, increase their energy level by 1
        for y, x in product(range(len(f)), range(len(f[0]))):
            f[y][x] += 1

        # for each octopus, increment surrounding octopi by 1
        flashed = set() # keep track of which octopi flashed
        added = True # this is dumb, but it works
        while added == True:
            added = False
            for y, x in product(range(len(f)), range(len(f[0]))):
                if (y,x) not in flashed and f[y][x] > 9:
                    # increase the energy level of all adjacent octopi by 1
                    added = True
                    flashed.add((y,x))
                    for i, j in adjacent(f, (y, x)):
                        f[i][j] += 1
        # reset flashed octopi to 0
        for y, x in flashed:
            f[y][x] = 0

        next(rounds)
        if len(flashed) == nfish:
            break

    return next(rounds)

def main():
    # start by getting file as a list of strings
    f = [[int(ch) for ch in l.strip()] for l in open(sys.argv[1], 'r')]

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()