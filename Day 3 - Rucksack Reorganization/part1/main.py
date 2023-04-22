with open('input.txt', 'r')as f:
 
sum_priority = 0
for rucksack in lines:
    middle = int(len(rucksack)/2)
    first, second = rucksack[:middle], rucksack[middle:]
    
    elements = {}
    for el in first:
        elements[el] = 1
    repeated = ''
    for el in second:
        if el in elements:
            repeated = el
            break
    
    priority = ord(repeated)
    if priority >= ord('a'):
        priority -= 96
    else:
        priority -= 38
    sum_priority += priority
print(sum_priority)
        
    
    