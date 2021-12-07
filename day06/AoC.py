import sys

# AoC template for python3

def part2(count:int, roundsleft:int, dyn:dict={}):
    # for each fish, we can figure out how many times it will duplicate itself
    # for each fish it generates, we can add another call
    # print(count, roundsleft)
    if (count >= roundsleft):
        return 0
    if (roundsleft - count - 1 in dyn):
        return dyn[roundsleft - count - 1]
    children = [part2(8, y, dyn) for y in range(roundsleft - count - 1, -1, -7)]
    ret = sum(children) + len(children)
    dyn[roundsleft - count - 1] = ret
    return ret # return the count of my own children, as well as the count of their children

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
   
    # each lanternfish has an internal timer that is a countdown
    # when it reaches 0, it resets itself to 6 and adds a new one with a count of 8
    # simulate thisscycle for 18 days

    lanternfish = [int(x) for x in f[0].split(",")]
    for i in range(80):
        # make a copy of the list
        for x in range(len(lanternfish)):
            if (lanternfish[x] > 0):
                lanternfish[x] -= 1
            else:
                lanternfish[x] = 6
                lanternfish.append(8)
    print("PART 1:", len(lanternfish))
    

    # if you make a call per fish, it will never finish
    # I think a dynamic programming solution is possible
    # start from bottom up, make a dynamic table of how many children each fish will generate if it is created in a certain window

    lanternfish = [int(x) for x in f[0].split(",")]
    dyn = {}
    count = [part2(i, 256, dyn) for i in lanternfish]
    print("PART 2:", sum(count) + len(count))


if __name__ == "__main__":
    main()
