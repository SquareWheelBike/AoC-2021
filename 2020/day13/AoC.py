import sys
from itertools import count

# part 1 only needs one fold
# answer is the number of points in the grid
def part1(time:int, buses:list) -> int:
    # find the first time where time % bus == 0
    c = count(start=time)
    for now in c:
        for bus in buses:
            if now % bus == 0:
                return (now - time) * bus

# got chinese remainder from https://medium.com/analytics-vidhya/chinese-remainder-theorem-using-python-25f051e391fc
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b # floor division
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# find the first place where each bus departs contiguously in order, including blank spaces
def part2(buses:list) -> int:
    # start at the first bus departure and only check those times
    a = [x - i % x for x, i in buses]
    n = [x for x, i in buses]       # n is the set of bus numbers
    return chinese_remainder(n, a)

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    time = int(f[0])
    buses = [int(bus) for bus in f[1].split(',') if bus != 'x']

    # part 1 only folds once, and counts the remaining points after fold
    print("Part 1:", part1(time, buses))

    # need the index of each bus for part 2
    buses = [(int(bus), i) for i, bus in enumerate(f[1].split(',')) if bus != 'x'] # this time we want the x's as well
    print("Part 2:", part2(buses))

if __name__ == "__main__":
    main()