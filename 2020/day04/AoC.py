import sys
import numpy
import math
import itertools

# AoC template for python3

def part1(passports:list):
    return [passport for passport in passports if all(key in passport for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])]

def part2(passports:list):
    # byr must be between 1920 and 2002
    # iyr must be between 2010 and 2020
    # eyr must be between 2020 and 2030
    # hgt must be a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl must be a valid hex color code, prefixed with #
    # ecl must be one of ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    # pid must be a nine-digit number, all of which must be digits
    # cid is not used in this puzzle
    passports = part1(passports) # only bother checking passports that have all the required fields
    passports = [passport for passport in passports if int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002]
    passports = [passport for passport in passports if int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020]
    passports = [passport for passport in passports if int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030]
    passports = [passport for passport in passports if (passport["hgt"][-2:] == "cm" and int(passport["hgt"][:-2]) >= 150 and int(passport["hgt"][:-2]) <= 193 or passport["hgt"][-2:] == "in" and int(passport["hgt"][:-2]) >= 59 and int(passport["hgt"][:-2]) <= 76)]
    passports = [passport for passport in passports if passport["hcl"][0] == "#" and len(passport["hcl"][1:]) == 6 and all(c in "0123456789abcdef" for c in passport["hcl"][1:])]
    passports = [passport for passport in passports if passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]]
    passports = [passport for passport in passports if len(passport["pid"]) == 9 and all(c in "0123456789" for c in passport["pid"])]
    return passports

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]

    # each passport is separated by a blank line, so split list by subgroups separated by blank lines
    rawpass = [" ".join(p) for k, p in itertools.groupby(f, lambda x: x != '') if k]
    # update passports to be a list of dictionaries of key:value pairs for each passport
    passports = [dict(item.split(":") for item in passport.split()) for passport in rawpass]
    print(len(part1(passports)))
    print(len(part2(passports)))

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()