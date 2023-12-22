#!/usr/env/python

# Initialize variables
result = 0
data = []

# Load input file
with open('input') as input_file:
    # Loop over lines in input file
    for line in input_file:
        # Put each line in array, and remove the railing
        # newline character
        data.append(line[:-1])

# Define the function which calculates the delta sequence
# (difference) of a given sequence.
def calculate_delta(sequence):
    # Empty variable
    delta_sequence = []
    # Loop over the given sequence excluding the final entry,
    # because the delta sequence is 1 shorter than the
    # sequence.
    for index in range(len(sequence) - 1):
        # Calculate the difference between the next value and
        # the current one, append this value to the delta
        # sequence.
        delta_sequence.append(int(sequence[index + 1]) - int(sequence[index]))
    # Once all values in the delta sequence are the same, we
    # are done. We test for this by converting the list to a
    # set. Sets contain only unique entries, so if the length
    # is 1, there is only one unique value stored.
    if len(set(delta_sequence)) != 1:
        # If this is not the case, recurse a level down and get the delta of the delta
        calculate_delta(delta_sequence)
    # After recursing, add the list of delta sequences to a 2D
    # list, this is done is reverse order, with the shortest
    # list being the first entry in the 2D list 
    delta_sequences.append(delta_sequence)

# Main loop, loop over every sequence
for sequence in data:
    # Empty up the 2D list of delta sequences
    delta_sequences = []
    # Split the sequence into an array and calculate the deltas
    # for it with the recursive function above.
    calculate_delta(sequence.split(" "))
    # Loop over all the delta sequences, minus one because we
    # always look one step ahead.
    for index in range(len(delta_sequences) - 1):
        # Append to the next sequence in the list the
        # difference between the last value of the current list
        # and the last value of the next list. This difference
        # is the predicted value.
        delta_sequences[index+1].append(int(delta_sequences[index][-1]) + int(delta_sequences[index+1][-1]))
    # This loop leaves us with the predicted value of the first
    # delta sequence, so we just add this value to the last
    # value of the sequence to get our next prediction.
    # This prediction is added to the result for the final
    # answer
    result += int(sequence.split(" ")[-1]) + delta_sequences[-1][-1]
# After looping over all the sequences, we just print the
# result
print(result)
