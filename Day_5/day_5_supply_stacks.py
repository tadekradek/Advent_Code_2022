# Link to Page
# https://adventofcode.com/2022/day/5

# Part 1
stack = [['F','H','M','T','V','L','D'],
['P','N','T','C','J','G','Q','H'],
['H','P','M','D','S','R'],
['F','V','B','L'],
['Q','L','G','H','N'],
['P','M','R','G','D','B','W'],
['Q','L','H','C','R','N','M','G'],
['W','L','C'],
['T','M','Z','J','Q','L','D','R']]


with open("input_commands.txt") as f:
    lines = f.readlines()

def cleaning_function(text):
    text = text.rstrip('\n').replace('move ','').replace('from ','').replace('to ','').split(' ')
    text = list(map(int,text))
    return text

lines = list(map(cleaning_function,lines))
lines

for i in lines:
    for j in range(0, i[0]):
        stack[i[2]-1].insert(0,stack[i[1]-1].pop(0))


for i in stack:
    print(i[0])


## Part 2 

stack = [['F','H','M','T','V','L','D'],
['P','N','T','C','J','G','Q','H'],
['H','P','M','D','S','R'],
['F','V','B','L'],
['Q','L','G','H','N'],
['P','M','R','G','D','B','W'],
['Q','L','H','C','R','N','M','G'],
['W','L','C'],
['T','M','Z','J','Q','L','D','R']]


with open("input_commands.txt") as f:
    lines = f.readlines()

def cleaning_function(text):
    text = text.rstrip('\n').replace('move ','').replace('from ','').replace('to ','').split(' ')
    text = list(map(int,text))
    return text

lines = list(map(cleaning_function,lines))
lines

for i in lines:
    for j in range(i[0],0,-1):
        stack[i[2]-1].insert(0,stack[i[1]-1].pop(j-1))


for i in stack:
    print(i[0])
