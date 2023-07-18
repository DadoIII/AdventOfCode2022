from itertools import chain

f = open('input8.txt', 'r')

heights = []
scenic_scores = []

line = f.readline().strip()

while line != '':
    temp_list = []
    for i in range(len(line)):
        temp_list.append(int(line[i]))
    heights.append(temp_list)
    scenic_scores.append([0] * len(line))
    line = f.readline().strip()

##heights = [[3,0,3,7,3],
##           [2,5,5,1,2],
##           [6,5,3,3,2],
##           [3,3,5,4,9],
##           [3,5,3,9,0]]
##
##scenic_scores = [[0,0,0,0,0],
##                 [0,0,0,0,0],
##                 [0,0,0,0,0],
##                 [0,0,0,0,0],
##                 [0,0,0,0,0]]


def reverse_2d(array):
    return [x [::-1] for x in array]

def flip_2d(array):
    return [list(r) for r in zip(*array)]


def get_scenic_score(x, y):
    score = 1
    score *= left(x,y)
    score *= right(x,y)
    score *= up(x,y)
    score *= down(x,y)
    return score

def left(x, y):
    trees = 0
    max_height = heights[y][x]
    current = -1
    while x > 0:
        x -= 1
        height = heights[y][x]
        trees += 1
        if height >= max_height:
            break
    return trees

def right(x, y):
    trees = 0
    max_height = heights[y][x]
    current = -1
    while x < len(heights) - 1:
        x += 1
        height = heights[y][x]
        trees += 1
        if height >= max_height:
            break
    return trees

def up(x, y):
    trees = 0
    max_height = heights[y][x]
    current = -1
    while y > 0:
        y -= 1
        height = heights[y][x]
        trees += 1
        if height >= max_height:
            break
    return trees

def down(x, y):
    trees = 0
    current = -1
    max_height = heights[y][x]
    while y < len(heights) - 1:
        y += 1
        height = heights[y][x]
        trees += 1
        if height >= max_height:
            break
    return trees

for i in range(len(heights)):
    for j in range(len(heights)):
        scenic_scores[i][j] = get_scenic_score(j, i)

#print(scenic_scores)
print(max(chain.from_iterable(scenic_scores)))
