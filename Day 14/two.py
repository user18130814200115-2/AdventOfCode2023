#!/usr/env/python

data = []
boxes = []
result = 0

with open('input') as input_file:
    for line in input_file:
        data = line[:-1].split(',')

for i in range(256):
    boxes.append({})

for sequence in data:
    hash_value = 0
    label = sequence.split('=')[0].split('-')[0]
    for character in label:
        hash_value += ord(character)
        hash_value = (hash_value * 17) % 256
    if sequence.count('-') > 0:
        try: boxes[hash_value].pop(label)
        except: pass
    else:
        boxes[hash_value][label] = sequence.split('=')[1]

for index, box in enumerate(boxes):
    jndex = 0
    for lens, focal in box.items():
        jndex += 1
        result += (1 + index) * (jndex) * int(focal)

print(result)
