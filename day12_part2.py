import copy

class Node():
    def __init__(self, height, visited = False):
        self.height = height
        self.visited = visited

f = open('input12.txt', 'r')

grid = []

line = f.readline().strip()

visited_nodes = []
row =  0


while line != '':
    inner_grid = []
    
    col = 0
    for character in line:
        if ord(character) >= 97 and ord(character) <= 122:
            inner_grid.append(Node(ord(character) - 96))
        elif character == 'S':
            inner_grid.append(Node(height = 1, visited = True))    
        elif character == 'E':
            inner_grid.append(Node(27))
            visited_nodes.append((row, col))
        col += 1

    row += 1
    grid.append(inner_grid)
    line = f.readline().strip()


count = 0
end = False
while not end:
    to_visit = []

    print(visited_nodes)
    for (y, x) in visited_nodes:
        height = grid[y][x].height

        #check if we reached the end
        if height == 1:
            print(count)
            end = True
            break

        #go left
        if x - 1 >= 0 and not grid[y][x-1].visited and grid[y][x-1].height + 1 >= height:
            to_visit.append((y, x-1))
            grid[y][x-1].visited = True
        
        #go right
        if x + 1 < len(grid[0]) and not grid[y][x+1].visited and grid[y][x+1].height + 1 >= height:
            to_visit.append((y, x+1))
            grid[y][x+1].visited = True

        #go up
        if y - 1 >= 0 and not grid[y-1][x].visited and grid[y-1][x].height + 1 >= height:
            to_visit.append((y-1, x))
            grid[y-1][x].visited = True

        #go down
        if y + 1 < len(grid) and not grid[y+1][x].visited and grid[y+1][x].height + 1 >= height:
            to_visit.append((y+1, x))
            grid[y+1][x].visited = True
    
    
    visited_nodes = copy.copy(to_visit)
    if len(visited_nodes) == 0:
        end = True
    count += 1
        




