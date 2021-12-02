# submitted using the java code, but I want to learn python better so redoing it here

# my answers:
# Part 1: 1480518
# Part 2: 1282809906

import sys # I want to pass filename on command line

if len(sys.argv) != 2:
    print("Usage: day2.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename) as f:
    lines = [line.split() for line in f]
# print(lines)

# PART 1

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

depth = 0
horizontal = 0

for line in lines:
    if line[0] == "forward":
        horizontal += int(line[1])
    elif line[0] == "up":
        depth -= int(line[1])
    elif line[0] == "down":
        depth += int(line[1])
    else:
        print("Error: Unknown command:", line[0])
        sys.exit(1)

print("Part 1:", abs(horizontal) * abs(depth))

# PART 2

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
#   It increases your horizontal position by X units.
#   It increases your depth by your aim multiplied by X.

depth = 0
horizontal = 0
aim = 0

for line in lines:
    if line[0] == "forward":
        horizontal += int(line[1])
        depth += aim * int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])
    elif line[0] == "down":
        aim += int(line[1])
    else:
        print("Error: Unknown command:", line[0])
        sys.exit(1)

print("Part 2:", abs(horizontal) * abs(depth))

