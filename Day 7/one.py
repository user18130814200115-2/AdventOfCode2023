#!/usr/env/python

data = []
sorted_data = []
result_data = []

# Load the input file, remove trailing newline characters
with open("input") as input_file:
    for line in input_file:
        data.append(line[:-1])   

# Sort the data according to card strength
sorted_data = sorted(data, key=lambda x: [int("AKQJT98765432 10".index(c)) for c in x])

# Get the unique cards and then check how many there are. We use this data to put the cards in a different list according to hand strength, but we otherwise keep the card strength sorting from earlier.

# If there is only one unique card, we have 5 of a kind
for game in sorted_data:
    s = set(game[:5])
    if len(s) == 1:
        result_data.append(game)

# If there are two, it is either full house, or four of a kind.

# Four of a kind means that the first card must either occur once, or four 
# times.
for game in sorted_data:
    s = set(game[:5])
    if len(s) == 2:
        if game[:5].count(game[0]) == 4:
            result_data.append(game)
        if game[:5].count(game[0]) == 1:
            result_data.append(game)

# Full house means that the first card must occur twice or thrice
for game in sorted_data:
    s = set(game[:5])
    if len(s) == 2:
        if game[:5].count(game[0]) == 2:
            result_data.append(game)
        elif game[:5].count(game[0]) == 3:
            result_data.append(game)

# If there are three unique cards, things get a little more difficult

# To catch 3 of a kind,, we must check thee positions, because the first 
# two could be singles.
for game in sorted_data:
    s = set(game[:5])
    if len(s) == 3:
        if game[:5].count(game[0]) == 3:
            result_data.append(game)
        elif game[:5].count(game[1]) == 3:
            result_data.append(game)
        elif game[:5].count(game[2]) == 3:
            result_data.append(game)

# To catch double pairs, we check two positions, because only one card can # be a single
for game in sorted_data:
    s = set(game[:5])
    if len(s) == 3:
        if game[:5].count(game[0]) == 2:
            result_data.append(game)
        elif game[:5].count(game[1]) == 2:
            result_data.append(game)
        
# if there are four cards of the same type, then there must be one pair
for game in sorted_data:
    s = set(game[:5])
    if len(s) == 4:
        result_data.append(game)

# Dump the remaining cards in the order we find them
for game in sorted_data:
    s = set(game[:5])
    if len(s) == 5:
        result_data.append(game)


# There are 1000 hands, so the highest rank is 1000
rank = 1000
total = 0

# Loop over all hands
for game in result_data:
    # Add the bet multiplied by the rank to the total
    total += int(game[6:]) * rank 
    # Move to the next rank
    rank -= 1

print(total)
