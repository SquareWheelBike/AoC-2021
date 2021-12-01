# input a text file into a list of integers
# each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine
readings = [int(i) for i in open('input.txt', 'r').read().splitlines()]
# count the number of times a depth measurement increases from the previous measurement
count = 0
for i in range(1, len(readings)):
    if readings[i] > readings[i-1]:
        count += 1
print("Part 1: " + str(count))

# part 2: create a list of sliding windows, 3 in length, and perform the same operation as part 1
windows = [readings[i:i+3] for i in range(len(readings)-2)]
count = 0
for i in range(1, len(windows)):
    if sum(windows[i]) > sum(windows[i-1]):
        count += 1
print("Part 2: " + str(count))