import sys

# Day 7
# The Treachery of Whales

def c1k(n:int):
    # sum from i=1 to k, i each time
    return int((n*(n+1))/2)

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    points = list(map(int, f[0].split(',')))

    # crabs can only move horizontally
    # points is a list of the horizontal position of each crab
    # crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring the least amount of fuel

    # I will just brute force for part 1
    # from 0 to max position, create a list of how much fuel it will take to get to each position
    fuelamts = {i:sum([abs(i-p) for p in points]) for i in range(1, max(points)+1)}
    print(min(fuelamts.values()))
    # NOT 321 (this was the key, I wanted the value)

    # part 2 is to find the minimum amount of fuel to get to each position, once again
    # but this time, each contiguous movement uses one more fuel, so 1 space uses 1 fuel, 2 spaces uses an additional 2, etc
    # so, we can use the sum formula with the movement cost to calculate the fuel cost
    fuelamts = {i:sum([c1k(abs(i-p)) for p in points]) for i in range(1, max(points)+1)}
    print(min(fuelamts.values()))

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()