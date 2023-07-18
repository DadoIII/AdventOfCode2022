from itertools import chain

f = open('input9.txt', 'r')

line = f.readline().strip()

positions = [(0,0)] * 10

spaces = [(0,0)]

def move_head(direction):
    Hx = positions[0][0]
    Hy = positions[0][1]
    
    if direction == 'L':
        vecX, vecY = -1, 0
    elif direction == 'R':
        vecX, vecY = 1, 0
    elif direction == 'U':
        vecX, vecY = 0, -1
    elif direction == 'D':
        vecX, vecY = 0, 1

    Hx += vecX
    Hy += vecY
    positions[0] = (Hx, Hy)

    for i in range(len(positions) - 1):
        move_tail(i)
    

def move_tail(i):
    Hx, Hy = positions[i][0], positions[i][1]
    Tx, Ty = positions[i+1][0], positions[i+1][1]
    #----------#
    # touching #
    #----------#
    
    if abs(Hx - Tx) + abs(Hy - Ty) <= 1:
        pass
    #diagonal, but still touching
    elif abs(Hx - Tx) == 1 and abs(Hy - Ty) == 1:
        pass
    
    #-------------------#
    # straight movement #
    #-------------------#
    
    #same column, head 2 places below tail
    elif Hx == Tx and Hy - Ty == 2:
        Ty += 1
    #same column, head 2 places above tail
    elif Hx == Tx and Hy - Ty == -2:
        Ty -= 1
    #same row, head 2 places to the right
    elif Hy == Ty and Hx - Tx == 2:
        Tx += 1
    #same row, head 2 places to the left
    elif Hy == Ty and Hx - Tx == -2:
        Tx -= 1

    #-------------------#
    # diagonal movement #
    #-------------------#
    
    #head is below and to the right
    elif Hx != Tx and Hy != Ty and Hy - Ty > 0 and Hx - Tx > 0:
        Ty += 1
        Tx += 1
    #head is below and to the left
    elif Hx != Tx and Hy != Ty and Hy - Ty > 0 and Hx - Tx < 0:
        Ty += 1
        Tx -= 1
    #head is above and to the right
    elif Hx != Tx and Hy != Ty and Hy - Ty < 0 and Hx - Tx > 0:
        Ty -= 1
        Tx += 1
    #head is above and to the left
    elif Hx != Tx and Hy != Ty and Hy - Ty < 0 and Hx - Tx < 0:
        Ty -= 1
        Tx -= 1

    positions[i+1] = (Tx, Ty)
    
    if i == (len(positions) - 2) and (Tx, Ty) not in spaces:
        spaces.append((Tx, Ty))

while line != '':
    direction, number = line.split(' ')
    for i in range(int(number)):
        move_head(direction)
    line = f.readline().strip()


print(len(spaces))
