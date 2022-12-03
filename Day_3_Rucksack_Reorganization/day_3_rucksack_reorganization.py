# Link to page
# https://adventofcode.com/2022/day/3

# Part 1

with open("input.txt") as f:
    lines = f.readlines()

lines = list(map(lambda x:x.rstrip('\n'),lines))
lines


#to check if the list contain only even numbers
length = list(map(lambda x: len(x),lines))
all([int(i)%2==0 for i in length])

#element of common for every first half and second half of the string
priority =  [list(set(i[:int(len(i)/2)]).intersection(set(i[int(len(i)/2):]))) for i in lines]

#sum of score
score = 0
for i in priority:
    for j in i:
        if j.isupper():
            score += ord(j)-38
        else:
            score += ord(j)-96

score

# Part 2

with open("input.txt") as f:
    lines = f.readlines()

lines = list(map(lambda x:x.rstrip('\n'),lines))

priorities = []
for i in range(0,301,3):
    priorities.append(list(set(lines[i]).intersection(set(lines[i+1])).intersection(set(lines[i+2]))))

priorities

score = 0
for i in priorities:
    for j in i:
        if j.isupper():
            score += ord(j)-38
        else:
            score += ord(j)-96

score
