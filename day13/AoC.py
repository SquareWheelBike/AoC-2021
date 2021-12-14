import sys
from itertools import groupby

# for each fold, fold the pattern along that line
# coordinates are (x, y)

def fold(points:set, fold:tuple) -> set:
    axis, line = fold # fold along 'x' or 'y' at line
    # fold along x at line
    if axis == 'x':
        points = {(line - (x - line), y) if x > line else (x, y) for x, y in points if x != line}
    # fold along y at line
    elif axis == 'y':
        points = {(x, line - (y - line)) if y > line else (x, y) for x, y in points if y != line}
    return points

# part 1 only needs one fold
# answer is the number of points in the grid
def part1(points:set, folds:list) -> int:
    # fold the points along the folds
    points = fold(points, folds[0]) # only actually do the first fold for part 1
    return len(points)

# part 2 completes all folds, then prints the message banner in the grid
def part2(points:set, folds:list) -> set:
    # fold the points along the folds
    for f in folds:
        points = fold(points, f)
    return points

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    # separate strings for points and folds
    points, folds = [list(group) for k, group in groupby(f, lambda x: x == "") if not k]
    # convert points to set of tuple coordinates
    points = {(int(i), int(j)) for i, j in [p.split(',') for p in points]}
    # each fold only needs an axis and a line
    folds = [(x, int(y)) for x, y in [f.replace('fold along ', '').split('=') for f in folds]]

    # part 1 only folds once, and counts the remaining points after fold
    print("Part 1:", part1(points.copy(), folds.copy()))

    # part 2 folds all folds, then prints the message banner in the grid
    print("Part 2:")
    grid = part2(points.copy(), folds.copy())   # apply all folds
    # find the bounding box
    x_max, y_max = max(grid, key=lambda x: x[0])[0], max(grid, key=lambda x: x[1])[1]
    layout = [''.join(['#' if (x, y) in grid else ' ' for x in range(x_max + 1)]) for y in range(y_max + 1)]
    for line in layout:
        print(line)


if __name__ == "__main__":
    main()