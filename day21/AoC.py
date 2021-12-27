import sys
from itertools import product, count, permutations
from copy import deepcopy
from functools import cache

def part1(p1, p2) -> int:
    d100 = 1
    p1score = 0
    p2score = 0
    while True:
        p1 += sum(((d100 + i) - 1) % 100 + 1 for i in range(3))
        d100 += 3
        p1 = (p1 - 1) % 10 + 1
        p1score += p1
        # print('p1:', p1, 'p1score:', p1score)
        if p1score >= 1000:
            return p2score * (d100 - 1)
        p2 += sum(((d100 + i) - 1) % 100 + 1 for i in range(3))
        d100 += 3
        p2 = (p2 - 1) % 10 + 1
        p2score += p2
        # print('p2:', p2, 'p2score:', p2score)
        if p2score >= 1000:
            return p1score * (d100 - 1)

possiblerolls = list({sum(p) for p in permutations([1,2,3], 3)}) # all possible roll scores for each turn, only one entry for each possibliity

# for each roll, create three copies of the next move
# return is tuple ints of how many times each player can win from here
@cache
def part2(p1:int, p2:int, p1score:int, p2score:int) -> tuple:
    return 0

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    starts = [int(l.split()[-1]) for l in f]

    print("Part 1:", part1(*starts))
    print("Part 2:", max(part2(*starts, 0, 0)))


if __name__ == "__main__":
    main()