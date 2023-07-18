
class Node:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.children = []
        self.files = []

    def add_child(self, child, name):
        names = map(lambda x: x[0], self.children)
        if name not in names:
            self.children.append((name, child))
            return True
        else:
            return False
        
    def add_file(self, name, size):
        names = map(lambda x: x[0], self.files)
        if name not in names:
            self.files.append((name, int(size)))
            return True
        else:
            return False

    def get_child(self, name):
        for i in range(len(self.children)):
            if self.children[i][0] == name:
                return self.children[i][1]
        return Exception('No child with that name')

    def get_children(self):
        return list(map(lambda x: x[1], self.children))

    def get_files(self):
        return list(map(lambda x: x[1], self.files))

    def get_parent(self):
        return self.parent

    def get_size(self):
        return sum(map(lambda x: x[1], self.files))


f = open('input7.txt', 'r')

line = f.readline().strip()
head = Node(None, '/')
current = head
line = f.readline().strip()

while line != '':
    if line[0] == '$':
        if line[2:4] == 'cd':
            folder_name = line[5:]
            if folder_name == '..':
                current = current.get_parent()
            else:
                current = current.get_child(folder_name)
    else:
        if line[:3] == 'dir':
            folder_name = line[4:]
            new = Node(current, folder_name)
            current.add_child(new, folder_name)
        else:
            size, name = line.split(' ')
            current.add_file(name, size)
            

    line = f.readline().strip()

directories = []

def find_sizes(node):
    children = node.get_children()
    total = 0
    for i in range(len(children)):
        total += find_sizes(children[i])

    files = node.get_files()
    for j in range(len(files)):
        total += files[j]

    directories.append(total)
    return total



total_space = 70_000_000
needed_space = 30_000_000

used_space = find_sizes(head)
directories.sort()

for i in range(len(directories)):
    if total_space - used_space + directories[i] >= needed_space:
        print(directories[i])
        break

