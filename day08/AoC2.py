import sys
from itertools import permutations

# After doing this once myself and seeing some peers' solutions, I figured I would try a brute force approach
# ie I am trying this with issac's method (https://github.com/kilbouri/advent-of-code 2021 day 8), but making sure I understand it
# this way is more brute-forcey, but makes good use of python builtins that I dont understand fully yet

# this only covers part 2

sevenseg = {"abcefg":0, "cf":1, "acdeg":2, "acdfg":3, "bcdf":4, "abdfg":5, "abdefg":6, "acf":7, "abcdefg":8, "abcdfg":9}  # dictionary of segments
strset = set(sevenseg.keys())

# l is the list of segments on the left side to be checked
# mapping is a dict from char -> char
def check(l:list, mapping:dict) -> bool:
    # map the permutation in mapping to characters in the l list
    # if the resulting set matches the sevenseg value list, then we have a match
    inRemapped = {
        "".join(sorted(map(mapping.get, val)))
        for val in l
    }
    # print(inRemapped)
    return inRemapped == strset

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    left = [[w.strip() for w in l.split(" | ")[0].split()] for l in f]
    right = [[w.strip() for w in l.split(" | ")[1].split()] for l in f]
    f = zip(left, right)

    total = 0
    
    for l, r in f:
        # if you feed a string to permutations, it treats it as a list of characters
        for p in permutations("abcdefg"):
            # same for zip, it treats the string as a list of chars, so this makes a dict of char -> char
            mapping = dict(zip(p, "abcdefg"))
            if check(l, mapping):
                rr = [
                    # for map, since second arg must be an iterable, then if you give it a string, it treats it as a list of chars
                    "".join(sorted(map(mapping.get, s))) # creates a list of strings, that should each match the sevenseg dict
                    for s in r
                ]

                # now convert the right hand side to decimal
                actualVal = "".join(
                    str(sevenseg[mapped])
                    for mapped in rr # this is a list of strings, concatenate the list of values that match the strings
                )

                total += int(actualVal)
                break
    print(total)
    


# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()