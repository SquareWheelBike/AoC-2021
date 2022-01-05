from sys import argv
from itertools import product, permutations
from operator import sub, add

# basically just copied issac's solution at https://github.com/kilbouri/advent-of-code/blob/main/2021/day19/part2.py
# I really dont like this puzzle and it is january 4, I just wanna be done

def rotate(p, rx, ry, rz):
    # rotates point p rA times around the A axis
    x, y, z = p
    for _ in range(rx):
        x, y, z = x, z, -y
    for _ in range(ry):
        x, y, z = z, y, -x
    for _ in range(rz):
        x, y, z = y, -x, z
    return x, y, z


def match(originBeacons, beacons, threshold=12):
    # originBeacons: the beacons relative to the world origin
    # beacons: the beacons we want to try to match onto originBeacons
    # threshold: the min number of beacons that must overlap

    for rotation in product(range(4), repeat=3):
        rotatedBeacons = [rotate(b, *rotation) for b in beacons]
        for originBeacon in originBeacons:
            for beacon in rotatedBeacons:
                offset = tuple(map(sub, originBeacon, beacon))
                beaconsOffset = set(
                    tuple(map(add, b, offset))
                    for b in rotatedBeacons
                )
                if len(beaconsOffset & originBeacons) >= threshold:
                    return beaconsOffset, offset


def main():
    with open(argv[1]) as file:
        file = file.read().split("\n\n")
        scanners = list(map(lambda snnr: {
            tuple(map(int, coord.strip().split(",")))
            for coord in snnr.splitlines()[1:]
        }, file))

    visited = set()
    distances = []

    def search(i, beacons, offset):
        print(f"Matching {i}")
        distances.append(offset)
        visited.add(i)

        for i, scanner in enumerate(scanners):
            if i in visited:
                continue

            matchRes = match(beacons, scanner)
            if matchRes:
                search(i, *matchRes)

    search(0, scanners[0], (0, 0, 0))

    print(f"Part 1: {len(visited)}")

    # find largest Manhattan distance between any 2 scanners
    maxMdist = max(
        sum(map(lambda a, b: abs(a-b), a, b))
        for a, b in permutations(distances, 2)
    )

    print(f"Part 2: {maxMdist}")


if __name__ == "__main__":
    main()
