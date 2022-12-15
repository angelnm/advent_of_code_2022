with open('input.txt', 'r')as f:
    lines = f.read().splitlines()
 
sum_priority = 0
for i in range(0, len(lines), 3):  
    r1 = lines[i +0]
    r2 = lines[i +1]
    r3 = lines[i +2]
    rucksacks = [r1, r2, r3]
    
    elements = {}
    for i in range(len(rucksacks)):
        rucksack = rucksacks[i]
        
        for el in rucksack:
            if el not in elements and i==0:
                elements[el] = 0
            elif el in elements and elements[el] == i-1:
                elements[el]=i
    
    repeated = ''
    for i in elements:
        if elements[i] == len(rucksacks)-1:
            repeated = i
            break
        
    priority = ord(repeated)
    if priority >= ord('a'):
        priority -= 96
    else:
        priority -= 38
    sum_priority += priority
print(sum_priority)

