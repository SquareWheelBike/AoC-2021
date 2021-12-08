import sys

sevenseg = {1:"cf", 2:"acdeg", 3:"acdfg", 4:"bcdf", 5:"abdfg", 6:"abdefg", 7:"acf", 8:"abcdefg", 9:"abcdfg", 0:"abcefg"}  # dictionary of segments

uniquelen = {x:y for x, y in sevenseg.items() if x in [1,4,7,8]}
given = [1,4,7,8]

# count number of character matches for each possible digit, with the current mapping
matches = {}
for x in sevenseg.keys():
    if x in given:
        continue
    matches[sum([sum([1 for ch in sevenseg[x] if ch in sevenseg[m]]) for m in given])] = x

def part2(l:list[str], r:list[str]) -> int:
    
    # mapping is a dict from str -> int, str is left side str, int is digit it corresponds to
    mapping = {}

    # start by finding the given digits from part 1
    for i in l:
        for x in uniquelen:
            if len(i) == len(uniquelen[x]):
                # print(i, x)
                mapping[i] = x
                break

    # now that we have an initial mapping, we can use it to find whatever remaining digits. 

    count = {}
    for x in l:
        if x in mapping.keys():
            continue
        count[x] = sum([sum([1 for ch in x if ch in m]) for m in mapping])
    # count overlap is unique for each unknown, if comparing to the known set
    # so, we can use that mapping, along with the mapping of sevenseg known digits, to find each digitstring
    # count: str -> count
    # matches: count -> digit
    for s, c in count.items():
        mapping[s] = matches[c]     

    # now that we have a mapping, we can use it to find the right side digits
    output = ""
    for i in r: # for each right side digit
        for x in mapping: # compare to each mapping
            if set(i) == set(x):
                output += str(mapping[x])
                break

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
    
    # if we use the preexisting mapping, we can find the order of digits to look for
    # ex: from the given set 1,4,7,8, we can find the mapping for the remaining digits based on which unfound should have the most matching characters in the known set
    print(sum([part2(l, r) for l, r in zip(left, right)]))


# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()