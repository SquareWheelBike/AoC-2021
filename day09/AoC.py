import sys
from itertools import product # for cartesian products
from numpy import prod # product of elements in iterable

# Advent of Code 2021 Day 9

# coord is y, x location tuple
# heightmap is a 2d list of ints
# returns list of points that are adjacent to the given coord
def adjacent(heightmap:list, coord:tuple) -> set:
    adjacent = set()
    y, x = coord
    # greatly reduced the number of points to check from big to <=9
    perm = product(range(max(0, y-1), min(y + 2, len(heightmap))), range(max(0, x-1), min(x + 2, len(heightmap[0]))))
    for i, j in perm:
        if i != y and j != x: # skip corners
            continue
        if y == i and x == j: # skip the current position
            continue
        adjacent.add((i, j)) # remaining four points are adjacent
    return adjacent

# look at points above, below, and to the left and right of each point
# heightmap is a 2d list of ints
# does not return points in the known list
def lowpoints(heightmap:list) -> set:
    lowpoints = set()
    # for each y pos
    for y, j in enumerate(heightmap):
        # for each x pos
        for x, l in enumerate(j):
            if all(l < heightmap[i][k] for i, k in adjacent(heightmap, (y, x))): # if current position lower than all the others
               lowpoints.add((y, x))    # add to list of lowpoints
    return lowpoints

# returns a list of lowpoints that are grouped with the coord lowpoint
# heightmap is the 2d list of ints
# coord is the base of the basin we are checking
# known is a list of known lowpoints to check against
# thisgrp is the list of lowpoints that are in the basin
# since each basin is walled in by 9 heights, we can just ignore 9 heights and add any other adjacents to the set
def basin(heightmap:list, coord:tuple, thisgrp=None) -> set:
    # thisgrp is what we are returning, we need a cache to keep track of lowpoints that are already in a basin
    if thisgrp is None:
        thisgrp = {coord} # start with own coord as group basis
    # get the list of lowpoints adjacent to the coord
    adjlow = {i for i in adjacent(heightmap, coord) if i not in thisgrp and heightmap[i[0]][i[1]] < 9}
    thisgrp.update(adjlow)
    # for each lowpoint added to basin in this pass, make a recursive call to check for more lowpoints
    for i in adjlow:
        basin(heightmap, i, thisgrp)
    return thisgrp

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    
    # if we consider each line as a heightmap, lava flows into the lowest position
    heightmap = [[int(l) for l in line] for line in f] # 2d list of height ints
    # perm = list(product(range(len(heightmap)), range(len(heightmap[0]))))

    # part 1, find lowest points
    lp = lowpoints(heightmap)
    risk = sum(heightmap[i][j] + 1 for i, j in lp) # sum of all lowpoints
    print(risk)
    # first goal is to find the low points, points lower than either adjacent position

    # points in lp -> list of points in the basin
    basins = {i:basin(heightmap, i) for i in lp} # basins will become a dict of lists of points, where each list is a group of clustered lowpoints
    # print(basins)
    sizes = [len(i) for i in basins.values()] # list of basin sizes
    print(prod(sorted(sizes, reverse=True)[:3])) # product of three largest basins

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()