#!/usr/env/python

# Manual data loading
time=44707080
distance=283113411341491
number=0

# Loop over every single possible charge length except 0 and max, because
# they definitely won't work.
for charge in range(1, time):
    # The distance is the charge level multiplied by the remaining time.
    # If this is greater than the record, increment the number of times we
    # can win
    if ((charge * (time - charge)) > distance):
        number += 1

print(number)
