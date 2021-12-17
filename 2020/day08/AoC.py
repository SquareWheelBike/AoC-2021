import sys

# Handheld Halting Problem

def main():
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]
    prg = [(l.split()[0], int(l.split()[1])) for l in f]
     #print(prg)

    # acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
    # jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
    # nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

    acc = 0 # accumulator
    isp = 0 # instruction pointer
    history = [] # history of instruction pointer values
    # continue executing instructions until we hit a repeat instruction
    while isp not in history:
        history.append(isp)
        #print(isp, prg[isp])
        if prg[isp][0] == 'acc':
            acc += prg[isp][1]
            isp += 1
        elif prg[isp][0] == 'jmp':
            isp += prg[isp][1]
        else:
            isp += 1
    print(acc)

    # now we either need to replace a jmp with a nop, or a nop with a jmp
    # create a list of isps with jmps or nops
    notacc = [pos for pos, (op, arg) in enumerate(prg) if op != 'acc']
    # print(notacc)
    # now, we can try one at a time to see if we can find a sequence that can reach the end of the program
    for pos in notacc:
        # create a copy of the prg
        prg2 = prg.copy()
        # replace the jmp with a nop or a nop with a jmp
        if prg2[pos][0] == 'jmp':
            prg2[pos] = ('nop', prg2[pos][1])
        else:
            prg2[pos] = ('jmp', prg2[pos][1])
        # reset the accumulator and isp
        # print("\ntry pos ", pos)
        # print(prg2)
        acc = 0
        isp = 0
        history = []
        # continue executing instructions until we hit a repeat instruction or we leave the program
        while isp not in history and isp < len(prg2) and isp >= 0:
            history.append(isp)
            #print(isp, prg2[isp])
            if prg2[isp][0] == 'acc':
                acc += prg2[isp][1]
                isp += 1
            elif prg2[isp][0] == 'jmp':
                isp += prg2[isp][1]
            else:
                isp += 1
        # if we get here, we found a sequence that can reach the end of the program
        if isp == len(prg2):
            print(acc)
            break

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()
