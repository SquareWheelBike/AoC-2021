import sys

sevenseg = {1:"cf", 2:"acdeg", 3:"acdfg", 4:"bcdf", 5:"abdfg", 6:"abdefg", 7:"acf", 8:"abcdefg", 9:"abcdfg", 0:"abcefg"}  # dictionary of segments

uniquelen = {x:sevenseg[x] for x in sevenseg if x in [1,4,7,8]}

def closest(target, mapping) -> (int, int):
    # a list of ints that could correspond to digitstr i by length
    print(target)
    print(mapping)
    print(target not in mapping)
    possibles = [j for j in sevenseg if len(target) == len(sevenseg[j]) and j not in mapping.values()] # list of possiblematches
    if (len(possibles) == 1):
        return possibles[0], 0
    # for each digit in each possible, check which other sevensegs also have that char
    # matches is a dict of int -> {chr:[ints]}
    # maps each possibility to a dict of characters in the possibility, and a list of ints that also will have thatchar
    print(possibles)
    matches = {digit:{ch:[d for d in sevenseg if d != digit and ch in sevenseg[d]] for ch in sevenseg[digit]} for digit in possibles}
    # use this map of matches to find the correct digit mapping
    # of these matches, whichever has the most ch matches that are also in mapping, is the one we want for checking
    # int -> int, left is digit, right is matches
    print(matches)
    countmatches = {s:sum([sum([1 for p in mapping if ch in p]) for ch in matches[s]]) for s in matches}
    # calculate the number of matches that could possibly be made
    expectedmatches = {s:sum([sum([1 for p in sevenseg if ch in sevenseg[p] and p != s]) for ch in sevenseg[s]]) for s in matches}
    countmatches = {s:int(expectedmatches[s] - countmatches[s]) for s in countmatches}
    print(countmatches)
    match = min(countmatches, key=countmatches.get) # get the key with the highest number of matches
    return match, countmatches[match]

def part2(l:list[str], r:list[str]) -> int:
    
    # mapping is a dict from str -> int, str is left side str, int is digit it corresponds to
        mapping = {}
        for i in l:
            for x in uniquelen:
                if len(i) == len(uniquelen[x]):
                    # print(i, x)
                    mapping[i] = x
                    break
        print(mapping)
        # now that we have an initial mapping, we can use it to find whatever remaining digits. 
        # we will start from the largest segment count, and work our way down
        # create a set of possible combinations for each as to where the digit is, and then once we have the whole set, pick the only one that works for all of them
        # print(l)
        while len(mapping) < len(l):
            # i is string, key is int digit best match for i, value is number of missing matches (lower is better)
            matches = {}
            for i in l:
                if i not in mapping:
                    best, bestcount = closest(i, mapping)
                    matches[i] = (best, bestcount)
            print(matches)
            bestkey = min(matches, lambda k:matches[k][1])
            mapping[bestkey] = matches[bestkey][0]

        # now that we have a mapping, we can use it to find the right side digits
        output = ""
        for i in r: # for each right side digit
            for x in mapping: # compare to each mapping
                if set(i) == set(x):
                    output += str(mapping[x])
                    break

        # print(output)
        print(r, output)
        return int(output)

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    left = [[w.strip() for w in l.split(" | ")[0].split()] for l in f]
    right = [[w.strip() for w in l.split(" | ")[1].split()] for l in f]
    
    
    # part 1 wants us to count the number of values in uniquelen that are only in the right side
    count = 0
    for r in right:
        for i in r:
            for x in uniquelen.values():
                if len(i) == len(x): # hint: 1,4,7,8 have unique lengths
                    # print(i, x)
                    count += 1
                    break
    print(count)

    # part 2: each left side entry is a list of ten mappings, and each corresponds to a digit in the right side
    # we need to find a mapping for each entry, and use it to find the right side digits
    # we can use the same dictionary of unique lengths, but we need to find the mapping for each left side entry
    print(sum([part2(l, r) for l, r in zip(left, right)]))


# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()