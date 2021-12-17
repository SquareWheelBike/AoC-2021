import sys
from itertools import groupby
from numpy import prod

# returns a dict of invalid nearby tickets and a list of their invalid fields
def findinvalid(valid, nearbytickets):
    invalid = {}
    for ticket in nearbytickets:
        for t in ticket:
            if not any(any(t in r for r in ran) for ran in valid.values()): # each ran is a list of ranges for that value
                if ticket not in invalid:
                    invalid[ticket] = []
                invalid[ticket].append(t)
    return invalid

# part 1 is to find the sum of fields of tickets that do not have any valid values
def part1(valid, myticket, nearbytickets):
    invalid = findinvalid(valid, nearbytickets)
    # each invalid ticket has a key 
    return sum(sum(t) for t in invalid.values())

def part2(valid, myticket, nearbytickets):
    # first, remove any invalid tickets from nearbytickets
    nearbytickets = [t for t in nearbytickets if t not in findinvalid(valid, nearbytickets).keys()]

    # entries are dicts of field:position
    positions = {}
    positionlists = [list(col) for col in zip(*nearbytickets)]
    for k, v in valid.items():
        # find a position where all tickets are valid for that position
        # for each key, find a position where all tickets are valid for that position
        for i, col in enumerate(positionlists):
            if i in positions.values(): # skip checking positions already taken
                continue
            if all(any(x in ran for ran in v) for x in col):
                positions[k] = i
                break
    
    # now, use the position map to multiply the six fields on my ticket that start with the word 'departure' together

    return 0

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]

    # now, parse the data from f into something we can use
    validranges, myticket, nearbytickets = [list(g) for k, g in groupby(f, key=lambda x: x != '') if k]  # k is true if not empty

    # valid can be a dict of possible fields and their valid ranges
    valid = {} 
    for r in validranges:
        r = r.split(':')
        valid[r[0]] = [range(int(i), int(j)+1) for i, j in [x.split('-') for x in r[1].split(' or ')]]
    # print(valid)

    myticket = tuple([int(x) for x in myticket[1].split(',')])
    # print(myticket)

    # nearbytickets is a list of lists of ints
    nearbytickets = [tuple([int(x) for x in y.split(',')]) for y in nearbytickets[1:]] # skip the first line
    # print(nearbytickets)

    print(part1(valid, myticket, nearbytickets))      
    # print(part2(f))  

if __name__ == "__main__":
    main()