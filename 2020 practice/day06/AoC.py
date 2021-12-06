import sys
import numpy
import math
import itertools

# AoC template for python3


def main():
    
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    groups = [" ".join(p).split() for k, p in itertools.groupby(f, lambda x: x != '') if k]
    
    answers = [set("".join(group)) for group in groups]
    print(sum([len(answer) for answer in answers]))

    # For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    answers = []
    for group in groups:
        allans = [letter for letter in alphabet if all(letter in ans for ans in group)]
        answers.append(allans)
    print(sum([len(answer) for answer in answers]))

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()