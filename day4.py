f = open('input4.txt', 'r')


def overlap(a, b):
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')

    if int(a1) > int(b2) or int(b1) > int(a2):
        return False
    else:
        return True


line = f.readline().strip()
num = 0
while line != '':
    a, b = line.split(',')
    if overlap(a, b):
        num += 1
    line = f.readline().strip()

print(num)
