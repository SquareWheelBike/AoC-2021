import sys
from itertools import permutations
from copy import deepcopy
import ast
from math import ceil, floor

# AoC template for python3

def addpairs(a, b):
    return [a,b]

# at most one split can happen per call
def evalsplits(l:list):
    for i, x in enumerate(l):
        if isinstance(x, list):
            state, l[i] = evalsplits(x)
            if state:
                return True, l
        else: 
            if x > 9:
                l[i] = [floor(x / 2), ceil(x / 2)]
                return True, l
    return False, l

# find the manitude of the final snailfish sum for p1
def magnitude(l) -> int:
    if isinstance(l, list):
        return 3 * magnitude(l[0]) + 2 * magnitude(l[1])
    else: 
        return l

# for adding to the nearest right
def addright(right, val):
    if isinstance(right, list):
        right[0] = addright(right[0], val)
    else:
        right += val
    return right

# for adding to the nearest left
def addleft(left, val):
    if isinstance(left, list):
        left[1] = addleft(left[1], val)
    else:
        left += val
    return left


def reduceline(l:list, d:int):
    left, right = l # get left and right children
    if type(left) is int and type(right) is int:
        return False, l, 0, 0
    if d >= 4:  # if depth is 4 or greater, and any children are lists, explode
        if type(left) is list:
            i, j = left
            return True, [0, addright(right, j)], i, 0
        if type(right) is list:
            i, j = right
            return True, [addleft(left, i), 0], 0, j
    else:
        # if depth is 3 or less, make a call to the children
        if type(left) is list:
            changes, left, i, j = reduceline(left, d + 1)
            if changes:
                return True, [left, addright(right, j)], i, 0
        if type(right) is list:
            changes, right, i, j = reduceline(right, d + 1)
            if changes:
                return True, [addleft(left, i), right], 0, j
        return False, [left, right], 0, 0


# f is a list of strings of lines to add
# adds the list of snail numbers, returns the final magnitude
def part1(f:list) -> int:
    snailsum = f[0]
    for i, line in enumerate(f[1:]):
        snailsum = addpairs(snailsum, line)
        flag = True
        while flag:
            flag, snailsum, j, k = reduceline(snailsum, 1)
            if flag:
                continue
            flag, snailsum = evalsplits(snailsum)
    return magnitude(snailsum)

# part 2 finds the largest magnitude sum from any permutation of two numbers in f
def part2(f:list) -> int:
    magnitudes = [part1(deepcopy(l)) for l in permutations(f, 2)]
    return max(magnitudes)

def main():
    # start by getting file as a list of strings
    f = [ast.literal_eval(l.strip()) for l in open(sys.argv[1], 'r')]

    print(part1(deepcopy(f)))
    print(part2(deepcopy(f)))


if __name__ == "__main__":
    main()
