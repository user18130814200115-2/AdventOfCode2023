#!/bin/sh

# This was my attempt at solving today's puzzle in POSIX Shell.
# At the end of the day, this code proved too slow and dash was
# not happy about the recursion. The lack of error messages
# about recursion depth ultimately lead me to just use python
# instead, even though shell is very well suited for this
# purpose

raw=$(cat input)
directions=$(printf "%s" "$raw" | head -n 1|\
    sed -e 's/L/2/g' -e 's/R/3/g')
map=$(printf "%s" "$raw" | tail -n +3 |\
    sed -E 's/(...) = .(...), (...)./\1;\2;\3/g')
max=$(printf "%s" "$directions" | wc -c)

step() {
    position="$1"
    index="$2"
    
    direction=$(printf "%s" "$directions" | cut -c $(($index % $max + 1)))
    position=$(printf "%s" "$map" | grep "^$position" | cut -d ';' -f $direction) 

    [ -z "$direction" ] && step $1 $2 && break
    [ -z "$position" ] && step $1 $2 && break

    index=$(($index + 1))

    
    echo "$position" "$index"
    [ "$position" = "ZZZ" ] && break
    [ $index -lt $max ] && step "$position" "$index"
}


step "AAA" 0
