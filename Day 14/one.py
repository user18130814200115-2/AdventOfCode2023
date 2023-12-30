#!/usr/env/python

data = []
result = 0

with open('input') as input_file:
    for line in input_file:
        data = line[:-1].split(',')

for sequence in data:
    hash_value = 0
    for character in sequence:
        hash_value += ord(character)
        hash_value = (hash_value * 17) % 256
    result += hash_value

print(result)
