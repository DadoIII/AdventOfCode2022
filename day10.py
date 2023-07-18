f = open('input10.txt', 'r')

cycle = 0
register = 1
pixels = ''

def draw_pixel():
    global pixels
    if cycle % 40 - 1 >= register - 1 and cycle % 40 - 1 <= register + 1:
        pixels += '#'
    else:
        pixels += '.'
    if cycle % 40 == 0:
        print(pixels)
        pixels = ''
        

line = f.readline().strip()

while line != '':
    if line[0] == 'a':
        value = int(line.split(' ')[1])
        cycle += 1
        draw_pixel()
        cycle += 1
        draw_pixel()
        register += value
    else:
        cycle += 1
        draw_pixel()
    line = f.readline().strip()



