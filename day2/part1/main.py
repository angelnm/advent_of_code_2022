with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

text2num = {'A':0, 'B':1, 'C':2, 'X':0, 'Y':1, 'Z':2}

result = 0
for battle in lines:
    opponent, yours = battle.split()
    
    opponent = text2num[opponent]
    yours = text2num[yours]
    
    result += yours+1
    
    if opponent == yours:
        result += 3
    elif (opponent+1)%3==yours:
        result += 6

print(result)