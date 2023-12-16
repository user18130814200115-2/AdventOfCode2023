#!/bin/sh

# 12 red, 13 green, 14 blue 

index=1
rm indexes

# Loop over the lines of the input file. There are 100 in this case, but you
# might want to use $(wc -l input) instead for dynamic lengths.
while [ $index -le 100 ]; do
    # These three lines all do essentially the same thing. They grab a single
    # line, grab a specific colour and its associated values. In doing so, every
    # line becomes multiple lines with every value of that colour in the given
    # game. I then turn the string into an equation where I subtract 1+ the
    # number of maximum cubes of the colour. This allows me to calculate the
    # sum, then if the sum is negative, there were enough cubes of the colour,
    # so the game was possible. We save the index of the impossible games to a
    # file.
    # I thought at first I had to calculate the impossible games, so I have to
    # reverse this working later. It would be better to just wc the lines with a
    # - sign in them.
    head -n $index input | tail -n 1 | grep -o "[0-9]* red" | sed -E 's/([0-9]*) red/\1-13/g' | bc | sed 's/-.*//g' | tr '\\n' ' ' | sed "s/.*[0-9].*/$index/g" >> indexes

    head -n $index input | tail -n 1 | grep -o "[0-9]* green" | sed -E 's/([0-9]*) green/\1-14/g' | bc | sed 's/-.*//g' | tr '\\n' ' ' | sed "s/.*[0-9].*/$index/g" >> indexes

    head -n $index input | tail -n 1 | grep -o "[0-9]* blue" | sed -E 's/([0-9]*) blue/\1-15/g' | bc | sed 's/-.*//g' | tr '\\n' ' ' | sed "s/.*[0-9].*/$index/g" >> indexes


    index=$(( index + 1))
done

# Here I grab all the indexes and make sure each index occurs only once. This is
# because sometimes a game is impossible because of multiple colours. Then I
# translate the several lines into one large sum. Because of the mistake
# earlier, This gives us the combined indexes of the IMPOSSIBLE games, to get
# the number of possible games, I subtract the IMPOSSIBLE form the total, which
# is 5050.
grep -o "[0-9]*" indexes | sort | uniq | tr '\\n' '+' | sed  -e 's/+$/)/g' -e 's/^+/5050-(/g' | bc
