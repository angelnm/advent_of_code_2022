with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

x = 1
cycle = 1
strength_at = [20, 60, 100, 140, 180, 220]
sum_strength = 0
for line in lines:
    value = 0
    if line[:4]=='noop':
        cycle += 1
    else:
        _, value = line.split()
        value = int(value)
        
        cycle += 2
        x += value
    
    if strength_at and cycle>=strength_at[0]:
        c_cycle = strength_at[0]
        if cycle == strength_at[0]:
            c_x = x
        else:
            c_x = x-value
        sum_strength += c_cycle*c_x    
            
        strength_at.pop(0)
print(sum_strength)