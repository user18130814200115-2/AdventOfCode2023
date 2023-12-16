#!/bin/sh

# First remove all letters, so we are left with just numbers
# Then we use sed to gram the first number on each line and save it to a file.
# The same is done for the last numbers to a different file
cat input | sed -Ee 's/[A-z]//g' -e 's/([0-9])[0-9]*/\\1/g' > first
cat input | sed -Ee 's/[A-z]//g' -e 's/[0-9]*([0-9])/\\1/g' > last

# Now we paste these files together, with nothing dividing them. This gives us
# combines numbers made of the first and last digits. I then turn every newline
# to plus signs. The version of dash I use is a little strange about escape
# characters, you probably want to use '\n' instead of '\\n'. I then use sed to
# remove the trailing plus sign from the final new line, and pipe everything
# into bc to calculate the sum.
paste -d '\\0' first last | tr '\\n' '+' | sed 's/+$//g' | bc


# The second answer is derrived in much the same way, only we first translate
# the words (one, two, three, etc) into their respective numbers. This first
# line turns 'one' into 'one1one'. The reason I keep the words on either side is
# so that words such as 'oneight' become '18' instead of '1ight'. These excess
# letters are removed later anyways.
cat input | sed -e 's/one/&1&/g' -e 's/two/&2&/g' -e 's/three/&3&/g' -e 's/four/&4&/g' -e 's/five/&5&/g' -e 's/six/&6&/g' -e 's/seven/&7&/g' -e 's/eight/&8&/g' -e 's/nine/&9&/g' > newinput

# The rest is the same
cat newinput | sed -Ee 's/[A-z]//g' -e 's/([0-9])[0-9]*/\\1/g' > first
cat newinput | sed -Ee 's/[A-z]//g' -e 's/[0-9]*([0-9])/\\1/g' > last
paste -d '\\0' first last | tr '\\n' '+' | sed 's/+$//g' | bc

# cleanup
rm first last newinput
