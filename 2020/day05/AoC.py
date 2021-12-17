import sys

# AoC template for python3

def calc_seat_id(ticket):
    # each ticket is a string of 10 characters
    lower = 0
    upper = 127
    # first 7 characters are the row
    for ch in ticket[:7]:
        if ch == 'F': # keep the lower half
            upper = int((upper + lower) / 2)
        else: # keep the upper half
            lower = int((upper + lower) / 2 + 1)
    row = lower
    # last 3 characters are the column
    lower = 0
    upper = 7
    for ch in ticket[7:]:
        if ch == 'R': # R takes the upper half of the row
            lower = int((upper + lower) / 2 + 1)
        else: # L takes the lower half of the row
            upper = int((upper + lower) / 2)
    col = lower
    return row * 8 + col

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]

    # PART 1
    #The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
    tickets = dict(zip(f, [calc_seat_id(t) for t in f]))
    print("Part 1: ",max(tickets.values()))
    
    # the ticket with IDs one above and one below missing is the missing ticket
    # Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
    # PART 2
    ids = sorted(tickets.values())
    missing = []
    for i in range(1, len(ids)-1):
        if ids[i-1] + 1 != ids[i]:
            missing.append(ids[i-1] + 1)
    print("Part 2: ", missing[0])

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()