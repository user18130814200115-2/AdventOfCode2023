#!/usr/env/python

data=[]
result = 0

with open('input') as input_file:
    for line in input_file:
        data.append(line[:-1].split(' '))

for line in data:
    # The number of unknown positions
    unknowns = line[0].count('?')
    # The number of possible combinations
    possibilities = pow(2, unknowns)
    # The key split into a list
    key = line[1].split(',')
    
    # Loop over all possible combinations
    for index in range(possibilities):
        # We convert the index to binary, where a 0 represents a . and a 1
        # represents a #
        raw = str(bin(index))[2:]
        # Pas this string with zeroes
        binary = '0' * (unknowns - len(raw)) + raw

        # Initialize variables
        sequences = []
        current_sequence_length = 0
        binary_index = 0
        # loop over each character in the original and count the number of # OR
        # the number of ? which we are interpreting as # in this current
        # solution
        for character in line[0]:
            match character:
                case '.':
                    if current_sequence_length > 0:
                        sequences.append(str(current_sequence_length))       
                    current_sequence_length = 0
                case '#':
                    current_sequence_length += 1
                case '?':
                    if binary[binary_index] == '1':
                        current_sequence_length += 1
                    else:
                        if current_sequence_length > 0:
                            sequences.append(str(current_sequence_length))       
                        current_sequence_length = 0
                    binary_index += 1
        if current_sequence_length > 0:
            sequences.append(str(current_sequence_length))       
         
        # If the sequences of # are the same as the provided key, add this as an
        # option.
        if sequences == key:
            result += 1
print(result)
