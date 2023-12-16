#!/usr/env/python
import numbers

data = []
result = 0

# Load the input into a 2D array where every entry is a tuple of the winning
# numbers and the scratched ones.
# I use a modified input file which does not contain the "Game x:" string, and
# where all spaces are collapsed into one. I could o this in python, but it was
# faster to just use sed.
with open('newnewinput') as input_file:
    for line in input_file:
        data.append(line.split(' | '))

# Loop over every tuple
for card in data:
    # Start with one point, because 0x2=0, this means that we always have
    # double the points we actually deserver, we fix this later
    points = 1
    # Split the winning numbers into an list
    for winning in card[0].split(' '):
        # Check if the winning numbers are in the list of scratched numbers.
        if winning in card[1].split(' '):
            # If they are, double the points
            points = points * 2
    # Check if we actually got points, or if we still have the initial value
    if points != 1:
        # Now we half the points to make up for the initial 1 point, and add the all together
        result += int(points / 2)
print(result)
