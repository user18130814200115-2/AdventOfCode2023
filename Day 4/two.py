#!/usr/env/python
import numbers

data = []
result = []
# Start with the number of scratchcards we get in the input file. This should
# be done in python instead of manually with wc.
total = 223

# Define recursive function, This gets a starting point in our list, and a
# number of cards said starting card won.
def counterboy(start, ran):
    # Make sure we add to the global total variable
    global total
    # Loop, starting with one card down the list
    for i in range(start+1, start+ran+1):
        # Increment the total number of cards
        total += 1
        # Recurse for the number of times the new card demands. This should
        # probably contain a check against cards which win 0 others to save
        # some cycles.
        counterboy(i, result[i])

# Open the modified input file (explanation in one.py)
with open('newnewinput') as input_file:
    # Loop over the file and split each game into a tuple with the winning
    # numbers and scratched numbers as items.
    for line in input_file:
        data.append(line.split(' | '))
# Loop over every tuple
for card in data:
    # To start, we earn 0 cards
    points = 0
    # Split both the winning numbers and scratched numbers into lists
    for winning in card[0].split(' '):
        if winning in card[1].split(' '):
            points += 1
    # Make a list of the points each card is worth 
    result.append(points)

# Now we start the counter by looping over every card and starting the
# recursion. This should probably also skip lines which are worth 0 cards. 
for index, value in enumerate(result):
    counterboy(index, value)

print(total)
