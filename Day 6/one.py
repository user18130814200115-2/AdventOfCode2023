#!/usr/env/python

# I just loaded in the data manually this time, instead of reading from a file
times=[44,70,70,80]
distances=[283,1134,1134,1491]
# These are the number of times we can beat the record per race,
# initialized as 0
numbers=[0,0,0,0]

# loop over the races
for index, time in enumerate(times):
    # loop over every single possible charge length except 0 and max,
    # because they definitely won't work.
    for charge in range(1, time):
        # The distance is the charge level multiplied by the remaining
        # time. If this is greater than the record, increment the number
        # of times we can win
        if ((charge * (time - charge)) > distances[index]):
            numbers[index] += 1

# Multiply the numbers together (should do for number in numbers but
# whatever)
print(numbers[1] * numbers[2] * numbers[3] * numbers[0])
