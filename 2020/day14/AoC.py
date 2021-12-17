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
        else:
            pos, val = [int(i) for i in line.replace("mem[","").split("] = ")]
            val &= mask[0]
            val |= mask[1]
            mem[pos] = val
    return sum(mem.values())

# returns a list of int addresses to write to
def parseaddr(addr, mask):
    addr = bin(addr)[2:] # change address to binary representation
    addr = '0' * (len(mask) - len(addr)) + addr # pad with 0's for processing
    # masks is a list of integers
    result = []
    for a, m in zip(addr, mask):
        if m == '1' or m == 'X':
            result.append(m)
        else:
            result.append(a)
    result = ''.join(result) # convert to string
    # now, compute every possible result of each mask, start with each x as 0 and then add each combination of x's as ones
    addresses = [result.replace('X', '0')]
    for i, m in enumerate(result):
        if m == 'X':
            for a in addresses.copy():
                addresses.append(a[:i] + '1' + a[i+1:])
    addresses = [int(a, 2) for a in addresses]
    return addresses

def part2(f):
    # f is the list of input strings
    # if it starts with a 'mask', then we set the mask
    mask = None
    mem = {}
    for line in f:
        if line.startswith('mask'):
            mask = line[7:]
        else:
            pos, val = [int(i) for i in line.replace("mem[","").split("] = ")]
            for a in parseaddr(pos, mask):
                mem[a] = val
    return sum(mem.values())

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]

    print(part1(f))      
    print(part2(f))  

if __name__ == "__main__":
    main()