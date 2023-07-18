import queue
f = open('input6.txt', 'r')

string = ''
line = f.readline().strip()

while line != '':
    string += line
    line = f.readline().strip()

f.close()

unique = ''

for i in range(len(string)):
    letter = string[i]
    #print(letter)
    #print(unique)
    #print(letter not in unique)
    if letter not in unique:
        unique = unique + letter
    else:
        index = unique.index(letter)
        unique = unique[index + 1:] + letter

    if len(unique) == 14:
        print(i + 1)
        break
        


