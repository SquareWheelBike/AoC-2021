import sys

def isvalid(prog, digits):
    z = 0
    for digit, dmo in zip(digits, prog):
        divisor, modifier, offset = dmo
        if z % 26 + offset == digit:
            z = z // divisor
        else:
            z = (z // divisor) * 26 + digit + modifier
    return not z

def parseprog(f):
    prog = []
    for i in range(0, 252, 18):
        prog.append((int(f[i+4].split()[-1]), int(f[i+5].split()[-1]), int(f[i+15].split()[-1])))
    return prog

def find_digits(left: int, right: int, find_max: bool = True):
    if find_max:
        if left + right <= 0:
            return 9, 9 + left + right
        else:
            return 9 - left - right, 9
    else:
        if left + right <= 0:
            return 1 - left - right, 1
        else:
            return 1, 1 + left + right

def calculate_version(instructions, find_max: bool = True) -> int:
    # very little idea of how this works, adapted it from someone else's solution
    instruction_sets = parseprog(instructions)
    version_number_digits: List = [None] * len(instruction_sets)
    left_digit_stack = []
    for i in range(len(instruction_sets)):
        if instruction_sets[i][0] == 1:
            left_digit_stack.append((i, instruction_sets[i]))
        else:
            left_i, left_instruction_set = left_digit_stack.pop()
            left_increment = left_instruction_set[2]
            right_increment = instruction_sets[i][1]
            version_number_digits[left_i], version_number_digits[i] = find_digits(left_increment, right_increment, find_max)
    return int(''.join([str(d) for d in version_number_digits]))

def part1(f):
    return calculate_version(f)

def part2(f):
    return calculate_version(f, False)

def main():
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    print(part1(f))
    print(part2(f))

if __name__ == "__main__":
    main()
