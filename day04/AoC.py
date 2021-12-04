import sys

# AoC template for python3

# boards is a list of lists with 5 rows and 5 columns
def checkwin(boards:list, calls:list, wins:list=[]):
    # check if any boards have a row or column where all entries are in calls
    # for each board
    for b in [bd for bd in boards if bd not in wins]:
        # for each row
        for r in b:
            # check if all entries are in calls
            if set(r).issubset(calls):
                return b
        # for each column
        for c in range(5):
            # check if all entries are in calls
            if set([r[c] for r in b]).issubset(calls):
                return b
    return False

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]

    # PART 1
    # need a list of words in line 1
    calls = [int(n) for n in f[0].split(',')]
    # now we need to injest the boards
    # each board is a list of 5 lists
    nboards = int(len(f) / 6)
    boards = [[[int(l) for l in j.split()] for j in f[(k*6+2):(k*6+7)]] for k in range(nboards)]
    
    for i in range(1, len(calls)):
        # check if any boards have a row or column where all entries are in calls
        # for each board
        b = checkwin(boards, calls[:i+1])
        if b != False:
            # sum the entries in the board not in calls
            print("Part 1:", sum([sum([l for l in r if l not in calls[:i+1]]) for r in b]) * calls[i])
            break
            

    # PART 2
    # part 2 answer
    wins = []
    i = 1
    while i < len(calls):
        # check if any boards have a row or column where all entries are in calls
        # for each board
        b = checkwin(boards, calls[:i+1], wins)
        if b != False:
            # add b to the list of winning boards so far
            wins.append(b)
            # if only one board is left not in wins, then we have the answer
            if len(wins) == nboards:
                win = wins[-1]
                print(win)
                s = sum([sum([c for c in r if c not in calls[:i+1]]) for r in win])
                # print(s)
                # print(calls[i])
                print("Part 2:", s * calls[i])
                break
            i -= 1 # go recheck for multiple wins
        i += 1

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()