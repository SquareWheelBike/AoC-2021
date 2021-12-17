import sys

# AoC day 9 from 2020

import itertools

def main():
    # start by getting file as a list of strings
    psize = 25
    f = [int(s) for s in [l.strip() for l in open(sys.argv[1], 'r')]]

    # print(sums)
    for i in range(psize, len(f)):
        if f[i] not in [sum(list(r)) for r in itertools.permutations(f[i-psize:i], 2)]:
            print("Part 1:", f[i])
            p1 = f[i]
            break

    # The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.
    
    # for each i, sum a sublist increasing in size until it passes part 1 result
    # result is the sum of the smallest and largest numbers in the sublist
    for i in range(len(f)-1):
        toobig = False
        for j in range(i+1, len(f)):
            s = f[i:j]
            ss = sum(s)
            if (ss) == p1:
                print("Part 2:", min(s) + max(s))
                # sum smallest and largest numbers in sublist
                exit()
            if ss > p1:
                toobig = True
                break
        if toobig == True:
            continue

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()