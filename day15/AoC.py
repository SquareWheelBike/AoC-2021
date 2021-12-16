import sys
from copy import deepcopy
from itertools import product, count

# note that part 2 will solve part 1 too, it just accounts for backwards paths,
# where part 1 is a very standard pathfinding algorithm (and faster by a lot than part 2)
def part1(cave):
    # each position is the sum of its own risk level and the lowest risk level of any upper or left position
    # so, do them one at a time incrementally
    cave[0][0] = 0
    for y in range(len(cave)):
        for x in range(len(cave[0])):
            if (y == 0 and x == 0):
                continue
            cave[y][x] += min(cave[y-1][x] if y > 0 else sys.maxsize, cave[y][x-1] if x > 0 else sys.maxsize)
    return cave[-1][-1]

# coord is y, x location tuple
# returns list of points that are adjacent to the given coord
def adjacent(coord:tuple, R:int, C:int) -> set:
    adjacent = set()
    y, x = coord
    # greatly reduced the number of points to check from big to <=9
    perm = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i, j in perm:
        if 0 <= y+i < R and 0 <= x+j < C:
            adjacent.add((y+i, x+j))
    return adjacent

# dijkstra's algorithm would be faster, but I wanted to do this myself
def part2(cave):
    R = len(cave)
    C = len(cave[0])
    cave[0][0] = 0 # need to set initial point risk to 0
    checked = {(0, 0):0} # the set of points we have already checked, with their involved risks
    queued = adjacent((0, 0), R, C) # the set of points that can be checked next pass
    while queued:
        nextqueue = set()
        for q in queued:
            adj = adjacent(q, R, C)
            checked[q] = min(checked[p] for p in adj if p in checked) + cave[q[0]][q[1]]
            adj = [p for p in adj if p not in checked]
            nextqueue.update(adj) 
        queued = nextqueue

    # now, check to see if any paths can be optimized
    # keep doing passes until everything settles
    queued = set(checked.keys()) # initial queue state is to recheck all points
    while queued:
        for q in queued.copy():
            # check if any adjacent points are lower risk
            y, x = q
            adj = adjacent(q, R, C)
            k = min(checked[(i, j)] for (i,j) in adj) + cave[y][x]
            if k < checked[q]:
                checked[q] = k
                queued.update(adj) # if I change, recheck all my adjacent points in case I provide a better path
            else:
                queued.remove(q) # if nothing about me changes, remove me from queued

    return checked[(R-1, C-1)]

def main():
    # start by getting file as a list of strings
    f = [[int(ch) for ch in l.strip()] for l in open(sys.argv[1], 'r')]

    # find the lowest cost path from top right to bottom left
    # my part 1 is just a standard pathfinding algorithm, so it's pretty fast
    print(part1(deepcopy(f)))

    # part 2 takes the part 1 grid and EXPANDS IT 5 times the size up and down
    # this conversion sucks but it still works in linear time so eat my ass issac I already know youre gonna complain about this
    f2 = []
    R = len(f)
    C = len(f[0])
    for i in range(R * 5):
        row = []
        for j in range(C * 5):
            new = f[i % R][j % C] + i // R + j // C
            while new > 9: # I will beat this question to death with a wet noodle
                new -= 9
            row.append(new)
        f2.append(row)

    # part 2 is massive and needs to account for backwards paths as well
    # takes about 30 seconds to run
    print(part2(f2))
        

if __name__ == "__main__":
    main()