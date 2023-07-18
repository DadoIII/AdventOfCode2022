f = open('input3.txt', 'r')


def get_priority(char):
    o = ord(char)
    if o >= 97 and o <= 122:
        return o - 96
    else:
        return o - 38

def get_matching(a, b, c):
    for i in range(len(a)):
        if a[i] in b and a[i] in c:
            return a[i]


a = f.readline().strip()
b = f.readline().strip()
c = f.readline().strip()
priorities = 0
while a != '':

    priority = get_priority(get_matching(a, b, c))
    priorities += priority
    a = f.readline().strip()
    b = f.readline().strip()
    c = f.readline().strip()

print(priorities)


