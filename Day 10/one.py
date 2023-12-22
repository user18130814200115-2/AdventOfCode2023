#!/usr/env/python

# Initialize variables
maze = []
steps = 0
class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class previous:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Load input into array
with open('input') as input_file:
    for row in input_file:
        maze.append(row)

# Get starting position
for y,row in enumerate(maze):
    for x,col in enumerate(row):
        if col == "S":
            position.y = y
            position.x = x
            previous.x = x
            previous.y = y

# Start by moving down (in my input the S is a |, you will need to adjust this
# for your input
position.y += 1
# Get the type of pipe in the current position to start the loop
value = maze[position.y][position.x]

while value != "S":
    # Iterate the number of steps we took
    steps += 1
    # Get the current pipe type
    value = maze[position.y][position.x]
    
    # More according to pipe type.
    # We use the previous position to determine which direction we are moving
    # in, we also store the current position to a variable so that we can use it
    # for the next round
    if value == "|":
        if previous.y < position.y:
            previous.x = position.x
            previous.y = position.y
            position.y += 1
        else:
            previous.x = position.x
            previous.y = position.y
            position.y -= 1
    elif value == "-":
        if previous.x > position.x:
            previous.x = position.x
            previous.y = position.y
            position.x -= 1
        else:
            previous.x = position.x
            previous.y = position.y
            position.x += 1
    elif value == "F":
        if previous.x > position.x:
            previous.x = position.x
            previous.y = position.y
            position.y += 1
        else:
            previous.x = position.x
            previous.y = position.y
            position.x += 1
    elif value == "J":
        if previous.y < position.y:
            previous.x = position.x
            previous.y = position.y
            position.x -= 1
        else:
            previous.x = position.x
            previous.y = position.y
            position.y -= 1
    elif value == "L":
        if previous.x > position.x:
            previous.x = position.x
            previous.y = position.y
            position.y -= 1
        else:
            previous.x = position.x
            previous.y = position.y
            position.x += 1
    elif value == "7":
        if previous.x < position.x:
            previous.x = position.x
            previous.y = position.y
            position.y += 1
        else:
            previous.x = position.x
            previous.y = position.y
            position.x -= 1
# The farthest away from the animal is simply halfway through the loop.
print(int(steps / 2))
