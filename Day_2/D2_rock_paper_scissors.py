# Link to page 
# https://adventofcode.com/2022/day/2

#Guide
# A - Rock
# B - Paper
# C - Scissors

# X - Rock - 1 point
# Y - Paper - 2 points
# Z - Scissors - 3 points

# Lost - 0 points
# Drawn- 3 points
# Won - 6 points

# Part 1

results={
    ("A","X"):4,
    ("A","Y"):8,
    ("A","Z"):3,
    ("B","X"):1,
    ("B","Y"):5,
    ("B","Z"):9,
    ("C","X"):7,
    ("C","Y"):2,
    ("C","Z"):6
}

with open('input.txt') as f:
    lines = f.readlines()
lines = list(map(lambda x: tuple(x.replace('\n',"").split(' ')),lines))

score = 0
for i in lines:
    score += results[i]

score

# Part 2 

# the second column now determines the outcome that you need to obtain thus determines your response to opponent strategy
# X - need to lose
# Y - need to draw
# Z - need to win


results = {
    ("A","X"):4,
    ("A","Y"):8,
    ("A","Z"):3,
    ("B","X"):1,
    ("B","Y"):5,
    ("B","Z"):9,
    ("C","X"):7,
    ("C","Y"):2,
    ("C","Z"):6
}


# X - need to lose
# Y - need to draw
# Z - need to win

# Map to cover the logic of transposed elements

# results = {
#     ("A","X","Loss"):("A","Z",3),
#     ("A","Y","Draw"):("A","X",4),
#     ("A","Z","Win"):("A","Y",8),
#     ("B","X","Loss"):("B","X",1),
#     ("B","Y","Draw"):("B","Y",5),
#     ("B","Z","Win"):("B","Z",9),
#     ("C","X","Loss"):("C","Y",2),
#     ("C","Y","Draw"):("C","Z",6),
#     ("C","Z","Win"):("C","X",7)
# }

outcomes = {
    ("A","Loss"):3,
    ("A","Draw"):4,
    ("A","Win"):8,
    ("B","Loss"):1,
    ("B","Draw"):5,
    ("B","Win"):9,
    ("C","Loss"):2,
    ("C","Draw"):6,
    ("C","Win"):7
}


with open('input.txt') as f:
    lines = f.readlines()
lines = list(map(lambda x: tuple(x.replace('\n',"").replace('X',"Loss").replace("Y","Draw").replace("Z","Win").split(' ')), lines))

score = 0
for i in lines:
    score += outcomes[i]

score
