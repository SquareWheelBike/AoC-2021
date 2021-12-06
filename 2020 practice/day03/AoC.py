import sys
import numpy
import math

# AoC template for python3

def treecount(forest:list, right:int, down:int):
    trees = 0
    for i in range(0, math.ceil(len(forest) / down)):
        if forest[i * down][(right*i) % len(forest[i])] == '#':
            trees += 1
    # print("right:", right, "down:", down, "trees:", trees)
    return trees


def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]

    # starting at the top left corner, move right 3 and down 1 until reaching the bottom
    # count the number of trees hit

    print("PART 1:", treecount(f, 3, 1))
    
    conf = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    counts = [treecount(f, *c) for c in conf]
    print("PART 2:", numpy.prod(counts))

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()