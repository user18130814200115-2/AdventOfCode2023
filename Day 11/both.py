#!/usr/env/python

# Establish Variables
data = []
coordinates = []
expand = [[],[]]
result = 0

# The expansion factor is 1 for the first puzzle and 999999 for the second
factor = 999999

# Load the input data
with open('input') as input_file:
    for line in input_file:
        # Line by line in array, remove trailing newline
        data.append(line[:-1])

# Expand the universe
for x in range(len(data[0])):
    column = [row[x] for row in data] 
    if len(set(column)) == 1:
        expand[1].append(x)
    if len(set(data[x])) == 1:
        expand[0].append(x)

# Get galaxy coordinates
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '#':
            coordinates.append([y, x])

# Get distances between galaxies
# Loop over all galaxies
for index, galaxy in enumerate(coordinates):
    # Loop over the remaining galaxies (the ones after the current one)
    for jndex in range(len(coordinates) - index - 1):
        # Calculate the horizontal and vertical distance between the current
        # galaxy and the others.
        result += abs(galaxy[0] - coordinates[jndex + index + 1][0])
        result += abs(galaxy[1] - coordinates[jndex + index + 1][1])

        # Check if we pass a stretch of expanded space, if we do, add the
        # expansion factor
        for row in expand[0]:
            if galaxy[0] > row > coordinates[jndex + index + 1][0]:
                result += factor
            elif galaxy[0] < row < coordinates[jndex + index + 1][0]:
                result += factor

        for col in expand[1]:
            if galaxy[1] > col > coordinates[jndex + index + 1][1]:
                result += factor
            elif galaxy[1] < col < coordinates[jndex + index + 1][1]:
                result += factor
print(result)

