import queue
f = open('input5.txt', 'r')

temp_stacks = [queue.LifoQueue() for _ in range(9)]
stacks = [queue.LifoQueue() for _ in range(9)]

for i in range(8):
    line = f.readline()
    for j in range(9):
        crate = line[j * 4 + 1]
        if crate != ' ':
            temp_stacks[j].put(crate)

for i in range(9):
    while not (temp_stacks[i].empty()):
        stacks[i].put(temp_stacks[i].get())

def move_crates(a, b, c):
    q = queue.LifoQueue()
    for _ in range(a):
        crate = stacks[b - 1].get()
        #print("crate " + str(crate) + " from " + str(b - 1) + " to " + str(c - 1))
        q.put(crate)
    while not (q.empty()):
        stacks[c - 1].put(q.get())

        

line = f.readline().strip()
print(line)
line = f.readline().strip()
print(line)
line = f.readline().strip()
print(line)
while line != '':
    line = line.replace('move ', '')
    line = line.replace(' from ', ',')
    line = line.replace(' to ', ',')
    a, b, c = line.split(',')
    move_crates(int(a), int(b), int(c))
    line = f.readline().strip()


top = ''
for i in range(9):
    top += stacks[i].get()

print(top)
