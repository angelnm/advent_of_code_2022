with open('input.txt', 'r') as fichero:
    lines = fichero.read().splitlines()
    
max_calories = 0    
current_calories = 0
for cal in lines:
    if cal != '':
        current_calories += int(cal)
    else:
        if current_calories > max_calories:
            max_calories = current_calories
        total = 0
print(max_calories)