with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

text2num = {'A':0, 'B':1, 'C':2}

result = 0
for battle in lines:
    opponent, strategy = battle.split()
    
    opponent = text2num[opponent]
    if strategy == 'X':
        yours = (opponent+2)%3
    elif strategy == 'Y':
        yours = opponent
    else:
        yours = (opponent+1)%3
    
    result += yours+1
    
    if opponent == yours:
        result += 3
    elif (opponent+1)%3==yours:
        result += 6

print(result)