# Link to Page
# https://adventofcode.com/2022/day/6


# Part 1
with open('input.txt') as f:
    lines = f.readlines()

code = lines[0]

for i in range(0, len(code)-3):
    if len(set(code[i:i+4]))==4:
        print(i+4)
        break
        
# Part 2
with open('input.txt') as f:
    lines = f.readlines()

code = lines[0]

for i in range(0, len(code)-13):
    if len(set(code[i:i+14]))==14:
        print(i+14)
        break
