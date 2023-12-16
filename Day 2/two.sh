#!/bin/sh

# 12 red, 13 green, 14 blue 

index=1
rm powers

while [ $index -le 100 ]; do
    # Get one specific line, get a specific the colour. Save only the numbers
    # of that colour, sort them numerically, and get the last of them (aka, the
    # highest
    red=$(head -n $index input | tail -n 1 | grep -o "[0-9]* red" | sed -E 's/([0-9]*) red/\1/g' | sort -g | tail -n 1)
    green=$(head -n $index input | tail -n 1 | grep -o "[0-9]* green" | sed -E 's/([0-9]*) green/\1/g' | sort -g | tail -n 1)
    blue=$(head -n $index input | tail -n 1 | grep -o "[0-9]* blue" | sed -E 's/([0-9]*) blue/\1/g' | sort -g | tail -n 1)

    # Multiple all three together, and increase the index.
    # For some reason, my shell sometimes fails at getting one of the colours.
    # While this did make for an interesting random number generator, it failed
    # to give the right answer. Therefore, I only increment the index when
    # successful. If not successful, we just run it again until it works. This
    # means the shell could hypothetically get stuck forever. But I found it
    # failed no more than 1 in 200 times.
    echo "$red * $green * $blue" | bc >> powers && index=$(( index + 1))
done

# Add all the powers together by translating newlines into + signs and removing
# the trailing +
cat powers | tr '\\n' '+' | sed  -e 's/+$//g' | bc
