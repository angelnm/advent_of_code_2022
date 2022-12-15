with open('input.txt', 'r') as fichero:
    lines = fichero.read().splitlines()
    
max_calories = [0, 0, 0]    
current_calories = 0
for cal in lines:
    if cal != '':
        current_calories += int(cal)
    else:
        if current_calories > max_calories[-1]:
            max_calories.pop(-1)
            
            inserted = False
            for i in range(len(max_calories)):
                if current_calories > max_calories[i]:
                    max_calories.insert(i, current_calories)
                    inserted = True
                    break
            if not inserted:
                max_calories.append(current_calories)
                
        current_calories = 0
        
sum_total = 0
for i in max_calories:
    sum_total += i       
print(sum_total)
