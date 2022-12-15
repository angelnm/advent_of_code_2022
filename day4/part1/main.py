with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

overlaps = 0
for assigment in lines:
    first, second = assigment.split(',')
    
    s1, e1 = first.split('-')
    s1 = int(s1)
    e1 = int(e1)
    s2, e2 = second.split('-')
    s2 = int(s2)
    e2 = int(e2)
    
    if s1<=s2 and e1>=e2:
        overlaps += 1
    elif s2<=s1 and e2>=e1:
        overlaps += 1
print(overlaps)
    