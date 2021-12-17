import sys
from itertools import product
from numpy import prod
from copy import deepcopy
import math

# day 12: Rain Risk

# rotate counterclockwise by angle degrees
def rotate(degrees: int, waypoint: tuple):
    y, x = waypoint
    rads = math.radians(degrees)

    dx = x * math.cos(rads) - y * math.sin(rads)
    dy = y * math.cos(rads) + x * math.sin(rads)

    return (round(dy), round(dx))

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    
    # each position has a single char direction and an integer value
    directions = {'N': (1, 0), 'S': (-1, 0), 'E': (0, 1), 'W': (0, -1)} # y, x coordinates
    rotations = {'N': {'L': 'W', 'R': 'E'}, 'S': {'L': 'E', 'R': 'W'}, 'E': {'L': 'N', 'R': 'S'}, 'W': {'L': 'S', 'R': 'N'}} # lookup is rotation[current][direction]

    coords = [(l[:1], int(l[1:])) for l in f]
    location = (0, 0) # start at 0,0, keep track of all positions visited
    rotation = 'E' # start facing east
    for direction, value in coords:
        # move
        y, x = location
        if direction in directions:
            dy, dx = directions[direction]
            location = (y + dy * value, x + dx * value)
        # rotate
        elif direction in rotations[rotation]:
            for _ in range(int(value / 90)):
                rotation = rotations[rotation][direction]
        # forward
        else:
            dy, dx = directions[rotation]
            location = (y + dy * value, x + dx * value)
        # print(direction, value, location, rotation)
    # answer is manhattan distance from 0,0
    print(abs(location[0]) + abs(location[1]))

    # part 2
    coords = [(l[:1], int(l[1:])) for l in f]
    location = (0, 0) # start at 0,0, keep track of all positions visited
    waypoint = (1, 10) # start waypoint at N1 E10
    rotation = 'E' # start facing east
    for direction, value in coords:
        # move
        y, x = waypoint
        if direction in directions: # move waypoint
            dy, dx = directions[direction]
            waypoint = (y + dy * value, x + dx * value)
        # rotate
        elif direction in {'L', 'R'}:
            if direction == 'L':
                waypoint = rotate(value, waypoint)
            else:
                waypoint = rotate(-value, waypoint)
        # forward
        else:
            dy, dx = location
            location = (dy + y * value, dx + x * value)
        # print(direction, value, location, waypoint)
    # answer is manhattan distance from 0,0
    print(abs(location[0]) + abs(location[1]))

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()
