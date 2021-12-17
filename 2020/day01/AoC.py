import sys
import itertools

# AoC template for python3

def main():
    # start by getting file as a list of strings
    f = [int(l.strip()) for l in open(sys.argv[1], 'r')]

    # PART 1
    # find the compination of two numbers that sum to 2020
    for i in itertools.combinations(f, 2):
        if sum(i) == 2020:
            print("Part 1:", i[0] * i[1])
            break

    # PART 2
    for i in itertools.combinations(f, 3):
        if sum(i) == 2020:
            print("Part 2:", i[0] * i[1] * i[2])
            break

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()