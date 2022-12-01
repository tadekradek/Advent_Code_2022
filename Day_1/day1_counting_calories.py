#link to the page
# https://adventofcode.com/2022/day/1

with open('values.txt') as f:
    lines = f.readlines()
lines = "".join(lines).split("\n\n")
lines = enumerate([i.rstrip('\n').split("\n") for i in lines])

dict ={}
for i in list(lines):
    dict[i[0]] = sum([int(i) for i in i[1]])

elves = sorted(dict.items(), key = lambda val: val[1], reverse= True)

# top 1 elf:
elves[0][1]

# top 3 elves:
elves[0][1] + elves[1][1] + elves[2][1]


## alternative solution, quite similar but without dictionary
with open('values.txt') as f:
    lines = f.readlines()

lines = "".join(lines).split("\n\n")

lines = list(enumerate([sum(list(map(int,i.rstrip('\n').split("\n")))) for i in lines]))
lines

elves = sorted(lines, key = lambda lines: lines[1], reverse= True)

# top 1 elf:
elves[0][1]

# top 3 elves:
elves[0][1] + elves[1][1] + elves[2][1]

