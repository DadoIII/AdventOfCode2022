f = open('input12.txt', 'r')

grid = []

line = f.readline().strip()

while line != '':
    inner_grid = []

    for character in line:
        if ord(character) >= 97 and ord(character) <= 122:
            inner_grid.append(ord(character) - 96)
        elif character == 'S':
            inner_grid.append(0)
        elif character == 'E':
            inner_grid.append(27)

    grid.append(inner_grid)
    line = f.readline().strip()

print(grid)

