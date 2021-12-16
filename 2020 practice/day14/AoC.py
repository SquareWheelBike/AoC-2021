import sys
from copy import deepcopy
from itertools import product, count

# mask will be a tuple of (0's position, 1's position)
# 0 pos is for bitwise and, 1 pos is for bitwise or
def parsemask(line):
    l = len(line)
    mask = [2 ** l - 1, 0]
    for i, ch in enumerate(line):
        if ch == '1':
            mask[1] |= 1 << (l - i - 1)
        elif ch == '0':
            mask[0] ^= 1 << (l - i - 1)
    return mask

def part1(f):
    # f is the list of input strings
    # if it starts with a 'mask', then we set the mask
    mask = None
    mem = {}
    for line in f:
        if line.startswith('mask'):
            mask = parsemask(line[7:])
            # print(bin(mask[0]), bin(mask[1]))
        else:
            pos, val = [int(i) for i in line.replace("mem[","").split("] = ")]
            # print(pos, val)
            val &= mask[0]
            val |= mask[1]
            mem[pos] = val
    return sum(mem.values())

# returns a list tuples of masks from parsemask for each possible floating point
def parsefloating(line):
    l = len(line)
    # masks is a list of integers
    masks = [parsemask(line)[1]] # starting point is all the ones positions
    for i, ch in enumerate(line):
        if ch == 'X':
            masks.extend([m | (1 << (l - i - 1)) for m in masks]) # extend the list with the new masks
    return [parsemask(str(bin(line)[2:])) for line in masks]

def part2(f):
    # f is the list of input strings
    # if it starts with a 'mask', then we set the mask
    masks = None
    mem = {}
    for line in f:
        if line.startswith('mask'):
            masks = parsefloating(line[7:])
            # print(masks)
        else:
            pos, val = [int(i) for i in line.replace("mem[","").split("] = ")]
            # print(pos, val)
            addresses = [(pos & mask[0]) | mask[1] for mask in masks]
            # print(addresses)
            for a in addresses:
                mem[a] = val
    return sum(mem.values())

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]

    print(part1(f))      
    print(part2(f))  

if __name__ == "__main__":
    main()