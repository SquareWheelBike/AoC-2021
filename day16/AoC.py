import sys
from itertools import count
from numpy import prod

# AoC Day 16: Packet Decoder

def part1(bitstr):
    # bits 0-2 are version, bits 3-5 are type
    # print('call', bitstr)
    if all(ch == '0' for ch in bitstr):
        return 0
    pver = int(bitstr[0:3], 2)
    ptyp = int(bitstr[3:6], 2)
    pos = 6 # position in bitstr, starts at 8 because we already read the first 6 bits

    # type 4 is a literal, a single integer value
    if ptyp == 4:
        while bitstr[pos] != '0':
            pos += 5
        return pver + part1(bitstr[pos+5:])
    
    # if not a literal, then it is an operator, which starts with a single bit, indicating the length type
    lengthid = int(bitstr[pos], 2)
    pos += 1
    if lengthid == 0:
        pos += 15
    else:
        pos += 11
    return pver + part1(bitstr[pos:])


def part2(bitstr):
    # bits 0-2 are version, bits 3-5 are type
    # version, type, length, subpackets, value
    me = {'ver': int(bitstr[0:3], 2), 'typ': int(bitstr[3:6], 2), 'len': 6, 'sub': [], 'val': 0}

    # type 4 is a literal, a single integer value
    if me['typ'] == 4:
        while True:
            me['val'] = (me['val'] << 4) + int(bitstr[me['len']+1:me['len']+5], 2)
            if bitstr[me['len']] == '0':
                me['len'] += 5
                break
            me['len'] += 5
        return me
    
    # if not a literal, then it is an operator, which starts with a single bit, indicating the length ID
    me['lid'] = int(bitstr[me['len']], 2)
    me['len'] += 1
    if me['lid'] == 0:  # 0 length ID means 15 bits for number of bits in subpackets
        length = int(bitstr[me['len']:me['len']+15], 2) 
        me['len'] += 15
        initial = me['len']
        while me['len'] - initial < length:
            sub = part2(bitstr[me['len']:])
            me['sub'].append(sub)
            me['len'] += sub['len']
    # 1 length ID means 11 bits for number of packets in subpackets
    else:
        length = int(bitstr[me['len']:me['len']+11], 2) 
        me['len'] += 11
        c = count(0)
        while next(c) < length:
            sub = part2(bitstr[me['len']:])
            me['sub'].append(sub)
            me['len'] += sub['len']

    # now, process the values of sub packets
    values = [sub['val'] for sub in me['sub'] if sub is not None]
    if me['typ'] == 0: # sum packets
        me['val'] = sum(values)
    elif me['typ'] == 1: # product packets
        me['val'] = prod(values)
    elif me['typ'] == 2: # min packet
        me['val'] = min(values)
    elif me['typ'] == 3: # max packet
        me['val'] = max(values)
    elif me['typ'] == 5: # greater than
        # 1 if first value is greater than second value, 0 otherwise (always have two sub packets)
        me['val'] = int(values[0] > values[1])
    elif me['typ'] == 6: # less than
        # 1 if first value is less than second value, 0 otherwise (always have two sub packets)
        me['val'] = int(values[0] < values[1])
    elif me['typ'] == 7: # equal
        # 1 if first value is equal to second value, 0 otherwise (always have two sub packets)
        me['val'] = int(values[0] == values[1])

    return me


def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    bitstr = ''.join(['{0:04b}'.format(int(ch, 16)) for ch in f[0]])

    print(part1(bitstr))
    print(part2(bitstr)['val'])

if __name__ == '__main__':
    main()