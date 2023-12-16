# Advent of Code 2023

This repository holds the scripts I used for
[https://adventofcode.com/2023](Advent of Code 2023).

To solve the challenges I use POSIX shell and python. All code is commented for
educational purposes. Keep in mind however that the aim of these scripts is to
solve the presented problems. They do not reflect best practices when coding,
nor are they representative of my general coding style. Quick-and-dirty is the
name of the game.

The programs written in POSIX shell might not work on your systems. The port of
dash i use has some particularities, especially when it comes to escape
sequences. For instance, where I use `'\\n'`, you might need to use `'\n'`.
Furthermore, the shell is rather unstable and sometimes fail randomly, meaning
my code requires more checks to avoid making a random number generator instead.
Lastly, I cannot use `while read` loop to loop over files, so I need to open
the file for each line, which is very bad practice. I also cannot use the
symbols `>|<&` in some strings because the shell will interpret them as
redirects.
