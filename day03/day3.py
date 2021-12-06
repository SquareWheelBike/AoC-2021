# 12 bits in each line
def countbits(filelist:list, nbits:int = 12):
    bitlist = [0] * nbits
    for line in filelist:
        # each line has a length
        for i in range(nbits):
            # each bit has a value
            if line[i] == "1":
                bitlist[i] += 1
            else:
                bitlist[i] -= 1
    return bitlist

def main():
    # start by getting file
    f = [l.strip() for l in open('input.txt', 'r')]
    nbits = 12

    # for each bit, negative favors zeros, positive favors ones, 0 means equal
    gamma = 0
    bitcounts = countbits(f, nbits)
    for i in range(nbits):
        if bitcounts[i] > 0:
            gamma = gamma | (1 << (nbits-i-1))

    mask = 2 ** nbits - 1
    epsilon = gamma ^ mask

    print("Part 1:", gamma * epsilon)

    # part 2

    # exygen generator rating: for each bit, if any bitstrings do not have the most common bit in that position, remove that bit
    o2 = f.copy()
    co2 = f.copy()
    for i in range(nbits):
        # if both are only length 1, then no point in going on
        if len(o2) == 1 and len(co2) == 1:
            break
        # lists to keep track of the bitstrings to remove
        ro2 = []
        rco2 = []
        # for each bit, find the most common bit
        if countbits(o2, nbits)[i] >= 0:
            bit = "1"
        else:
            bit = "0"
        # then, check the current bit position for each bitstring
        # if not match, remove that bitstring
        for j in o2:
            if j[i] == bit:
                ro2.append(j)

        if countbits(co2, nbits)[i] >= 0:
            bit = "1"
        else:
            bit = "0"
        for j in co2:
            if j[i] != bit:
                rco2.append(j)
        # remove tagged bitstrings, if at least one is left
        if len(ro2) > 0:
            o2 = ro2
        if len(rco2) > 0:
            co2 = rco2
    # print(int(o2[0], 2))
    # print(int(co2[0], 2))
    print("Part 2:", int(o2[0], 2) * int(co2[0], 2))
    # 2981085

if __name__ == "__main__":
    main()