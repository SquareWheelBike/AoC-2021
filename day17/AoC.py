import sys
from itertools import product
from math import ceil, sqrt
from re import findall

# find the max y position possible while still being in the area
# since we do hit y=0 on the way down every time, the max initial velocity up is the minimum y under 0, minus 1 because of acceleration
def part1(area) -> int:
    ymin = abs(area[2]) - 1 # will overshoot if we point it at the actual minimum, thanks to yv -= 1 each time
    return ((ymin * ymin) + ymin) // 2   # derived this with a sum, using basis that ymin is the initial velocity, and yv=0 at the highest point

# check if a point is in the target area
def inarea(x, y, area):
    if area[0] <= x <= area[1] and area[2] <= y <= area[3]:
        return True
    else:
        return False

# check if a point is past the target area
def pastarea(x, y, area):
    if y < area[2] or x > area[1]:
        return True
    else:
        return False


def part2(area) -> int:
    # this one is just getting brute forced

    # need to determine the bounds of velocities that will work
    xvmin = ceil((sqrt(1 + 8 * area[0]) - 1) / 2)  # derived this with a sum, where x reaches 0 velocity as it collides with the left wall
    xvmax = area[1]  # max velocity must be the far side of the area, or it will just pass right through (+1 be)
    yvmin = area[2]  # min velocity must be the minimum y, or it will just pass right through
    yvmax = abs(area[2]) - 1 # any faster and it will pass right through the target area after finishing its ark

    tries = product(range(xvmin, xvmax + 1), range(yvmin, yvmax + 1))
    valid = set()

    # now, try all the possible velocities
    for dx, dy in tries:
        initial = (dx, dy)  # record the initial velocity for this try
        x, y = dx, dy       # start at the initial velocity
        while not pastarea(x, y, area): # while we haven't passed the target area
            if inarea(x, y, area): # if we're in the target area, add it to the valid set
                valid.add(initial)
                break
            if dx > 0: # decrease x until it reaches 0
                dx -= 1
            dy -= 1     # y continually falls faster
            x += dx     # apply the velocity to the position
            y += dy     # apply the velocity to the position

    return len(valid)

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    # find all integers in the single line
    area = [int(i) for i in findall(r'-?\d+', f[0])]
    print("Part 1:", part1(area))
    print("Part 2:", part2(area))

if __name__ == "__main__":
    main()
