import sys

# part 1 just simulates what is happening (brute force solution)
# this runs in O(2^n) time, where n is the number of rounds 
# (10 is small enough it still runs instantly, only reaches a few thousand characters)
def part1(sim:str, synth:dict) -> int:
    # initial is a string
    # if two characters in any position match a pair in insertions, insert the value for that key inbetween the pair

    # this is horrible but it got me the answer in a reasonable amount of time
    for x in range(10):
        sim  = "".join([c + synth[c + sim[i+1]] if i < len(sim) - 1 and c + sim[i+1] in synth else c for i, c in enumerate(sim)])

    # now that we have the final string, find the character that is most common
    return sim.count(max(set(sim), key=sim.count)) - sim.count(min(set(sim), key=sim.count))

# part 2 is the same as part 1, but heavily optimized to go to round 40
# instead of keeping track of the whole string, we only keep track of counts of sets of two characters, and individual character counts
# this finishes in O(n) time, where n is the number of rounds
def part2(sim:str, synth:dict) -> int:
    # counted is a dict of possible characters and their counts
    counted = {c:0 for c in set("".join(synth.keys()))}
    for ch in sim:
        counted[ch] += 1
    # also convert sim into a dict of string pairs and their counts, add all possible combinations now  
    original = sim
    sim = {c:0 for c in synth.keys()}
    base = sim.copy()   # base is a starting point for each new round
    for i in range(1, len(original)):
        sim[original[i-1] + original[i]] += 1

    # now, apply the rounds
    for x in range(40):
        new = base.copy()    # next round needs to be counted separately
        for k, v in sim.items():                # for each k strpair, v count in sim
            new[k[0] + synth[k]] += v
            new[synth[k] + k[1]] += v
            counted[synth[k]] += v
        sim = new # store this round's calculation in sim

    # now, subtract the biggest value from the smallest value and return
    return max(counted.values()) - min(counted.values())

            

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]

    template = f[0] # starting point string
    insertions = {l:r for l, r in [line.split(" -> ") for line in f[2:]]} # dictionary of insertions
    print(part1(template, insertions))
    print(part2(template, insertions))

if __name__ == "__main__":
    main()