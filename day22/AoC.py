import sys
from itertools import product, count, permutations
from copy import deepcopy
from re import findall

def part1(f:list) -> int:
    cubes = set() # set of all cubes that are on
    for i, line in enumerate(f):
        state, locations = line
        # print(f'{i}: {state} {locations}')
        x1, x2, y1, y2, z1, z2 = locations
        x1 = max(x1, -50)
        x2 = min(x2, 50)
        y1 = max(y1, -50)
        y2 = min(y2, 50)
        z1 = max(z1, -50)
        z2 = min(z2, 50)
        locations = set(product(range(x1, x2+1), range(y1, y2+1), range(z1, z2+1)))
        # print(f'{len(locations)} locations')
        if state == 'on':
            cubes.update(locations)
        else:
            cubes.difference_update(locations)
    return len(cubes)

def part2(f:list) -> int:
    cubes = set() # set of all cubes that are on
    for i, line in enumerate(f):
        state, locations = line
        print(f'{i}: {state} {locations}')
        x1, x2, y1, y2, z1, z2 = locations
        locations = set(product(range(x1, x2+1), range(y1, y2+1), range(z1, z2+1)))
        print(f'{len(locations)} locations')
        if state == 'on':
            cubes.update(locations)
        else:
            cubes.difference_update(locations)
    return len(cubes)

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    steps = [(line.split(' ')[0], [int(i) for i in findall(r'-?\d+', line)]) for line in f]

    print("Part 1:", part1(deepcopy(steps)))
    # print("Part 2:", part2(deepcopy(steps)))


if __name__ == "__main__":
    main()