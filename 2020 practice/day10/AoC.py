import sys

# Joltage!

def main():
    # start by getting file as a list of strings
    f = [int(l.strip()) for l in open(sys.argv[1], 'r')]
    f.append(0) # start at 0
    f.sort()
    f.append(f[-1] + 3) # your phone is 3 jolts higher than second highest rating
    diff1 = sum([1 for i in range(len(f)-1) if f[i+1] - f[i] == 1])
    diff3 = sum([1 for i in range(len(f)-1) if f[i+1] - f[i] == 3])
    print(diff1 * diff3)

    # configs will be a list of configs to get to each rating
    # first config is 1 config, for 0 joltage adapters in list
    configs = [1]
    for i in range(1, len(f)):
        # for each index, add the number of configs to get to that index
        # add a new config for each new i
        configs.append(0)
        for j in range(i):
            # add the number of configs to get to the index i
            # if difference is less than 3, then it is removeable, and thus, adds a config to configs
            if f[i] - f[j] <= 3:
                configs[i] += configs[j]
    # the most configs will be accumulated at the end of the list
    print(configs[-1])

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()
