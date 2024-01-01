#!/usr/env/python

# Initialize variables
data = []
result = 0
result_one = 0

# Load input into a list
with open('input') as input_file:
    for line in input_file:
        data.append(line[:-1])

# This is the main function, it takes a starting position, and a direction to
# calculate the direction of the light
def traject(y, x, dy, dx):
    # We loop until the beam is done
    while True:
        # Calculate the new position based on the direction vector
        y = y + dy
        x = x + dx
        # If we have already checked this position and direction, we can stop
        # the causations, this saves loads of time.
        name = str(y) + ',' + str(x) + ',' + str(dy) + ',' + str(dx)
        if name not in trajected:
            # If the trajectory has not yet been calculated, add it to the set
            # of valuated trajectories and continue.
            trajected.add(name)
        else:     
            break

        # Fist we check if we have left the bounds of the playing field, if so,
        # we stop, if no, we continue
        if x > -1 and x < 110 and y > -1 and y < 110:
            # Add the current coordinates to the energized set
            energized.add(str(x) + ',' + str(y))
            
            # Get the mirror in the current position and adjust the vector
            # accordingly
            match data[y][x]:
                case '\\':
                    if dy != 0:
                        dx = dy
                        dy = 0
                    else:
                        dy = dx
                        dx = 0
                case '/':
                    if dy != 0:
                        dx = -dy
                        dy = 0
                    else:
                        dy = -dx
                        dx = 0
                case '|':
                    if dx != 0:
                        dy = 1
                        dx = 0 
                        # Splitters will start a new trajectory
                        traject(y, x, -1, 0)
                case '-':
                    if dy != 0:
                        dy = 0
                        dx = 1 
                        # Splitters will start a new trajectory
                        traject(y, x, 0, -1)
        else:
            break

# Loop over the 4 possible starting sides left, top, right, bottom
for side in range(4):
    # Loop over the 110 possible locations on that side
    for i in range(110):
        # Reset the trajected and energized sets
        trajected = set()
        energized = set()
        # Run the appropriate starting trajectory based in the side and location
        match side:
            case 0:
                traject(i, -1, 0, 1)
            case 1:
                traject(-1, i, 1, 0)
            case 2:
                traject(i, 110, 0, -1)
            case 3:
                traject(110, i, -1, 0)
        # Save the number of energized tiles if it is higher than the current
        # highest number
        if len(energized) > result:
            result = len(energized)
        # The result for puzzle one is simply the first result we get, so we
        # store this on in its own variable
        if result_one == 0:
            result_one = len(energized)

# Print the number of energized tiles for the first trajectory
print(result_one)
# Print the highest number of energized tiles
print(result)
