import sys
from functools import reduce

# Advent of Code 2021 Day 9
closing = [")", "}", "]", ">"]
opening = ["(", "{", "[", "<"]

def checkBalanced(line: str) -> str:
    # queue of brackets to check
    q = []
    for c in line:
        if c in opening:
            q.append(c)
        elif c in closing:
            ch = q.pop()
            if closing.index(c) != opening.index(ch):
                return c
    return ""

def autocomplete(line: str) -> str:
    # queue of brackets to check
    q = []
    for c in line:
        if c in opening:
            q.append(c)
        elif c in closing:
            ch = q.pop()
    q.reverse()
    ret = "".join([closing[opening.index(c)] for c in q])
    return ret

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]

    points = {")": 3, "]": 57, "}": 1197, ">": 25137, "": 0}
    score = [points[checkBalanced(l)] for l in f]
    print(sum(score))

    acs = [autocomplete(l) for l in f if checkBalanced(l) == ""]
    points = {")": 1, "]": 2, "}": 3, ">": 4}  # redefine points for part 2
    scores = [reduce(lambda x, y: x * 5 + y, [points[c] for c in l]) for l in acs]
    scores.sort()
    print(scores[int(len(scores)/2)])

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()
