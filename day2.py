f = open('input2.txt', 'r')


def add_score(opponent, result):
    score = 0
    me = '' 
    if opponent == 'A':
        if result == 'X':
            score += 0
            me = 'scissors'
        elif result == 'Y':
            score += 3
            me = 'rock'
        elif result == 'Z':
            score += 6
            me = 'paper'
            
    elif opponent == 'B':
        if result == 'X':
            score += 0
            me = 'rock'
        elif result == 'Y':
             score += 3
             me = 'paper'
        elif result == 'Z':
            score += 6
            me = 'scissors'
            
    elif opponent == 'C':
        if result == 'X':
            score += 0
            me = 'paper'
        elif result == 'Y':
            score += 3
            me = 'scissors'
        elif result == 'Z':
            score += 6
            me = 'rock'

    if me == 'rock':
        score += 1
    elif me == 'paper':
        score += 2
    elif me == 'scissors':
        score += 3
            
    return score
            


line = f.readline()
score = 0
while line != '':
    opponent, result = line.strip().split(' ')
    score += add_score(opponent, result)
    line = f.readline()

print(score)


