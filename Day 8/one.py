#!/usr/env/python

# I modified the input file a bit with sed, this makes it easier to load into
# python. Undoubtedly, this can also be done with python directly
# tail -n + 2 input | sed -E 's/(...) = .(...), (...)./\1;\2;\3/g' > instructions

with open('instructions') as input_file:
    directions={}
    for line in input_file:
        modline=line[:-1].split(';')
        # Here we save all the instructions as a dictionary with 
        # POSITION:LEFT;RIGHT
        directions[modline[0]]=modline[1] + ';' + modline[2]

# Also load in the LEFT/RIGHT instructions (first line of the input file)
with open('input') as input_file:
    for line in input_file:
        instructions = line[:-1]
        break

def step(position, index):
    global new_position
    global new_index

    # Grab the current instruction, we use a modulo of the length of the string
    # to loop over the instructions if we run out
    instruction=instructions[index % len(instructions)]

    if instruction == "L":
        # If the instruction is LEFT, we look up our current position in the
        # dictionary and take the FIRST item
        new_position = directions[position].split(';')[0]
    else:
        # Otherwise we take the second item
        new_position = directions[position].split(';')[1]

    new_index = index + 1
   
# Give the starting data
new_position="AAA"
new_index=0
# Loop until we find ZZZ
while new_position != "ZZZ":
    step(new_position, new_index)

# When we find ZZZ, print the number of steps it took
print(new_index)
