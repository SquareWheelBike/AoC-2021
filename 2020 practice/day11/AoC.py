import sys
from itertools import product
from copy import deepcopy

# day 11: seating system

# coord is y, x location tuple
# heightmap is a 2d list of ints
# returns list of points that are adjacent to the given coord
def adjacent(seats:list, coord:tuple) -> set:
    adjacent = set()
    y, x = coord
    # greatly reduced the number of points to check from big to <=9
    perm = [(dy, dx) for dy, dx in product([-1, 0, 1], [-1, 0, 1]) if (dy, dx) != (0, 0)]
    for i, j in perm:
        if 0 <= y+i < len(seats) and 0 <= x+j < len(seats[0]):
            adjacent.add((y+i, x+j))
    return adjacent

# inview returns a list of points that are in view of the given coord
def inview(seats:list, coord:tuple) -> set:
    adjacent = set()
    y, x = coord
    # greatly reduced the number of points to check from big to <=9
    perm = [(dy, dx) for dy, dx in product([-1, 0, 1], [-1, 0, 1]) if (dy, dx) != (0, 0)]
    for i, j in perm: # perm is the set of directions
        coeff = 1 # coeff determines the length of the line of sight in that direction
        while 0 <= y+i*coeff < len(seats) and 0 <= x+j*coeff < len(seats[0]):
            if seats[y+i*coeff][x+j*coeff] != '.': # continue until finding a non floor spot
                adjacent.add((y+i*coeff, x+j*coeff))    # add seat to the list of inview seats
                break # dont bother checking beyond the first visible seat in direction in perm
            coeff += 1
    return adjacent

def main():
    # start by getting file as a list of strings
    seats = [l.strip() for l in open(sys.argv[1], 'r')]
    f = deepcopy(seats)
    # L means empty seat
    # # means occupied seat
    # . means floor

    # for each round, some rules must be applied:
    # if a seat is empty (L) and there are no occupied seats around it, it becomes occupied (#)
    # if a seat is occupied (#) and four or more seats are occupied around it, it becomes empty (L)
    # else nothing changes
    # floor (.) never changes

    # keep going until no more changes occur
    anychanges = True
    changemap = {'L':'#', '#':'L'}
    plane = list(product(range(len(f)), range(len(f[0]))))
    while anychanges:
        changing = set() # set of seats that will change, changes are made after evaluation
        for y, x in plane:
            if f[y][x] == 'L':
                # check that not seats are occupied around it
                if not any(f[y][x] == '#' for y, x in adjacent(f, (y, x))):
                    changing.add((y, x))
            if f[y][x] == '#':
                # check that four or more seats are occupied around it
                if len([(i, j) for i, j in adjacent(f, (y, x)) if f[i][j] == '#']) >= 4:
                    changing.add((y, x))
        # apply changes
        for y, x in changing:
            f[y] = f[y][:x] + changemap[f[y][x]] + f[y][x+1:]
        anychanges = len(changing) > 0 # set changes flag
    print(sum(sum(1 for c in row if c == '#') for row in f))


    # for part 2, we do the same thing but occupied seats become unoccupied if they cannot see more than 5 seats occupied in any direction
    f = deepcopy(seats)
    anychanges = True
    changemap = {'L':'#', '#':'L'}
    while anychanges:
        changing = set() # set of seats that will change, changes are made after evaluation
        for y, x in plane:
            if f[y][x] == 'L':
                # check that not seats are occupied around it
                if not any(f[y][x] == '#' for y, x in inview(f, (y, x))):
                    changing.add((y, x))
            if f[y][x] == '#':
                # check that four or more seats are occupied around it
                if len([(i, j) for i, j in inview(f, (y, x)) if f[i][j] == '#']) >= 5:
                    changing.add((y, x))
        # apply changes
        for y, x in changing:
            f[y] = f[y][:x] + changemap[f[y][x]] + f[y][x+1:] # this is the only way to change a single character in the string
        anychanges = len(changing) > 0 # set changes flag
    print(sum(sum(1 for c in row if c == '#') for row in f))

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()
