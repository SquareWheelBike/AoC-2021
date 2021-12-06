import sys

# AoC template for python3

def passcheck(line:str):
    # check if passwd is valid
    # return True if valid, False if not
    line = line.split(":")
    ran = tuple(line[0].strip().split()[0].split("-"))
    letter = line[0].strip().split()[1]
    passwd = line[1].strip()
    count = 0
    # print("range:", ran, "letter:", letter, "passwd:", passwd)
    for l in passwd:
        if l == letter:
            count += 1
    return True if count >= int(ran[0]) and count <= int(ran[1]) else False

def passcheck2(line:str):
    # valid if one of the two positions is the same letter
    line = line.split(":")
    ran = tuple(line[0].strip().split()[0].split("-"))
    letter = line[0].strip().split()[1]
    passwd = line[1].strip()
    return (passwd[int(ran[0])-1] == letter) ^ (passwd[int(ran[1])-1] == letter)

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]

    # PART 1
    valid = filter(passcheck, f)
    print("PART 1:", len(list(valid)))

    # PART 2
    valid = filter(passcheck2, f)
    print("PART 2:", len(list(valid)))

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()