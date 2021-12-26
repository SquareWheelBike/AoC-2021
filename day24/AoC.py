import sys
from itertools import product, count, permutations
from copy import deepcopy

globalvars = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

# inp a - Read an input value and write it to variable a.
def inp(line, w):
    assert(line[0] == 'inp' and len(line) == 2)
    a = line[1]
    globalvars[a] = int(w)
    return True

def add(line):
    assert(line[0] == 'add' and len(line) == 3 and line[1] in globalvars)
    x, y = line[1], line[2]
    a = globalvars[x] if x in globalvars else int(x)
    b = globalvars[y] if y in globalvars else int(y)
    globalvars[x] = a + b
    return True

def mul(line):
    assert(line[0] == 'mul' and len(line) == 3 and line[1] in globalvars)
    x, y = line[1], line[2]
    a = globalvars[x] if x in globalvars else int(x)
    b = globalvars[y] if y in globalvars else int(y)
    globalvars[x] = a * b
    return True

def div(line):
    assert(line[0] == 'div' and len(line) == 3 and line[1] in globalvars)
    x, y = line[1], line[2]
    a = globalvars[x] if x in globalvars else int(x)
    b = globalvars[y] if y in globalvars else int(y)
    if b == 0:
        return False
    globalvars[x] = a // b
    return True

def mod(line):
    assert(line[0] == 'mod' and len(line) == 3 and line[1] in globalvars)
    x, y = line[1], line[2]
    a = globalvars[x] if x in globalvars else int(x)
    b = globalvars[y] if y in globalvars else int(y)
    if b <= 0 or a < 0:
        return False
    globalvars[x] = a % b
    return True

def eql(line):
    assert(line[0] == 'eql' and len(line) == 3 and line[1] in globalvars)
    x, y = line[1], line[2]
    a = globalvars[x] if x in globalvars else int(x)
    b = globalvars[y] if y in globalvars else int(y)
    globalvars[x] = int(a == b)

# inputs is a stack of the 14 characters to take, already in int form
def evalline(line, inputs=None):
    if line[0] == 'inp':
        return inp(line, inputs.pop(0))
    elif line[0] == 'add':
        return add(line)
    elif line[0] == 'mul':
        return mul(line)
    elif line[0] == 'div':
        return div(line)
    elif line[0] == 'mod':
        return mod(line)
    elif line[0] == 'eql':
        return eql(line)
    else:
        return False

def runprog(f, inputs):
    # if any(1 > i > 9 for i in inputs):
    #     return False
    globalvars = {'w': 0, 'x': 0, 'y': 0, 'z': 0}   # reset program before starting
    for line in f:
        if not evalline(line.split(), inputs):
            return False
    return globalvars['z'] == 0 # success if w is 0 and program finishes

# for each position, try current position, up one, and down one
# if any of those are in the list, then it's a duplicate
def part1(f):
    inpsize = sum([1 for l in f if l.split()[0] == 'inp'])
    # tries = {}  # integers tried so far
    testcombos = [[9,8,7,6,5,4,3,2,1]] * inpsize
    for p in product(*testcombos):
        if runprog(f, list(p)):
            return int(''.join(map(str, p)))
    return 0

def main():
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    print(part1(deepcopy(f)))
    # print(part2(deepcopy(f)))

if __name__ == "__main__":
    main()
