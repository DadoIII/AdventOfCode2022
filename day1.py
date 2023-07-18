f = open('input1.txt', 'r')


line = f.readline()
max_counts = []
count = 0
while line != '':
    if (line != '\n'):
        count += int(line)
    else:
        if len(max_counts) < 3:
            max_counts.append(count)
        else:
            min_count = min(max_counts)
            if count > min_count:
                max_counts[max_counts.index(min_count)] = count
        count = 0
    line = f.readline()

print(max_counts)
print(sum(max_counts))
