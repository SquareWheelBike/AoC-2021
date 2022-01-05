import sys
from itertools import product, count, permutations
from copy import deepcopy

# NOTE - this is a very slow solution, and I'm not sure if it is the best solution
# part 1 runs quickly, part 2 takes a good 30 mins and like 8gb of ram

# uses a brute forcey dijkstra's algorithm, finds shortest path to literally every possible state until it finds the goal

COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
# only let each one reenter at its proper column
XCOORD = {'A': 3, 'B': 5, 'C': 7, 'D': 9}

# nonwalls is the set of all non-wall coordinates
nonwalls = set()
for y, line in enumerate(('#...........#',
                          '###A#B#C#D###',
                          '###A#B#C#D#')):
    for x, char in enumerate(line):
        if char != '#':
            nonwalls.add((x, y))

def adjacent(cur, x, y):
    # returns a list of adjacent coordinates that are open to move into, from the given coordinate
    adj = []
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if (x+dx, y+dy) in nonwalls and cur[y+dy][x+dx] == '.':
            adj.append((x+dx, y+dy))
    return adj


def possibleMoves(cur: tuple, complete: set) -> list:
    # returns a list of tuples of possible moves, and the cost of each move
    # ignores moves that include a solid placement (a mole is where it should stay)
    moves = []
    possibles = nonwalls.difference(complete) if complete else nonwalls
    for x, y in possibles:
        char = cur[y][x]
        if char == '.':
            continue
        for i, j in adjacent(cur, x, y):
            # if descending and not in proper column, skip
            if j > y and XCOORD[char] != i:
                continue
            move = list(cur)
            move[y] = move[y][:x] + '.' + move[y][x+1:]
            move[j] = move[j][:i] + char + move[j][i+1:]
            moves.append((tuple(move), COST[char]))
    return moves


def updatecomplete(cur: tuple, complete: set, goal: tuple):
    ret = deepcopy(complete) if complete else set()
    for x, y in nonwalls.difference(ret):
        char = cur[y][x]
        if char == '.':
            continue
        if char == goal[y][x] and ((x, y+1) in ret or y == len(cur)-1):
            ret.add((x, y))
    return ret if ret else None


def part1(f: tuple, GOAL: tuple) -> int:
    # use a kind of dijkstra's algorithm to find the shortest set of movements to get to the goal
    dijkstra = {f: (0, None)}
    thisround = {f}
    curcutoff = 0
    while GOAL not in dijkstra:
        print('this round', len(thisround))
        nextround = set()
        for cur in thisround:
            curcost, complete = dijkstra[cur]
            for move, cost in possibleMoves(cur, complete):
                if move not in dijkstra or curcost + cost < dijkstra[move][0]:
                    dijkstra[move] = (
                        curcost + cost, updatecomplete(move, complete, GOAL))
                    nextround.add(move)

        # dont bother continuing to check dead paths, also remove dead paths from the dijkstra dict to save memory
        cutoff = max({len(v) if v else 0 for x, v in dijkstra.values()}) - 1
        if cutoff > curcutoff:
            curcutoff = cutoff
            dijkstra = {k: v for k, v in dijkstra.items(
            ) if v[1] and len(v[1]) >= cutoff}
            nextround = {k for k in nextround if k in dijkstra}

        thisround = nextround
    return dijkstra[GOAL][0]


def part2(f: tuple, GOAL: tuple) -> int:
    for y, line in enumerate(('#...........#',
                              '###A#B#C#D###',
                              '###A#B#C#D#',
                              '###A#B#C#D#',
                              '###A#B#C#D#')):
        for x, char in enumerate(line):
            if char != '#' and (x, y) not in nonwalls:
                nonwalls.add((x, y))
    return part1(f, GOAL)


def main():
    # start by getting file as a list of strings
    f = [l.replace(' ', '#').strip() for l in open(sys.argv[1], 'r')][1:4]

    GOAL = ('#...........#',
            '###A#B#C#D###',
            '###A#B#C#D#')
    print("Part 1:", part1(tuple(f), GOAL))

    addition = ['  #D#C#B#A#',
                '  #D#B#A#C#']
    f = f[:2] + addition + f[2:]
    GOAL = ('#...........#',
            '###A#B#C#D###',
            '###A#B#C#D#',
            '###A#B#C#D#',
            '###A#B#C#D#')
    print("Part 2:", part2(tuple(f), GOAL))


if __name__ == "__main__":
    main()
