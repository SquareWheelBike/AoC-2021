import sys
from itertools import product, groupby
from copy import deepcopy

# used for debugging, prints the current image edged with unknown points
def printimage(image, unknown='.'):
    xvals = [x for x, y in image.keys()]
    yvals = [y for x, y in image.keys()]
    minx = min(xvals) - 1
    mai = max(xvals) + 2
    miny = min(yvals) - 1
    maxy = max(yvals) + 2
    for y in range(miny, maxy):
        for x in range(minx, mai):
            print((image[(x, y)] if (x, y) in image else unknown), end='')
        print()
    print()
    return None

# make sure that any possible unknown spots that are in range of a known spot are in the image to be
def extendimage(image, unknown='.'):
    for x, y in list(image.keys()):
        for coord in product([x-1, x, x+1], [y-1, y, y+1]):
            if coord not in image:
                image[coord] = unknown
    return image

# create the lookup value from the points surrounding the point
def lookup(x, y, image, unknown='.'):
    location = 0
    for j, i in product([y-1, y, y+1], [x-1, x, x+1]):
        if (i, j) in image: # get value of known point
            append = 1 if image[(i, j)] == '#' else 0
        else:               # get value of unknown point
            append = 1 if unknown == '#' else 0
        location = (location << 1) + append
    return location

# image is the set of known points
# imagemap is the lookup table
# unknown is the value of the infinite set of other unknown points not in the image
def enhance(image, imagemap, unknown='.'):
    # before next round, make sure that all points surrounding any known points are in the image, for calculations next pass
    image = extendimage(image, unknown)
    
    nextpoints = {}
    for x, y in image.keys():
        # get the lookup value for the point
        # if the output is 1, add the surrounding points to the next points
        nextpoints[(x, y)] = imagemap[lookup(x, y, image, unknown)]
    # next pass needs its unknown positions to be calulated as well
    unknown = imagemap[0] if unknown == '.' else imagemap[511]
    return nextpoints, unknown

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1])]
    imagemap, imagestr = [list(g) for k,g in groupby(f, key=lambda s: s!='') if k] # separate the image from the map by blank line
    imagemap = ''.join(imagemap) # convert map to single string
    # also convert the image to a set of tuple points
    image = {}  
    for y, line in enumerate(imagestr):
        for x, char in enumerate(line):
            if char == '#':
                image[(x, y)] = '#'

    # part 1 applies two rounds of enhancement
    p1 = deepcopy(image)
    unknown = '.'
    for i in range(2):
        p1, unknown = enhance(p1, imagemap, unknown)
    print(sum([1 for val in p1.values() if val == '#']))

    # part 2 applies 50 rounds of enhancement
    p2 = deepcopy(image)
    unknown = '.'
    for i in range(50):
        p2, unknown = enhance(p2, imagemap, unknown)
    print(sum([1 for val in p2.values() if val == '#']))


if __name__ == '__main__':
    main()
