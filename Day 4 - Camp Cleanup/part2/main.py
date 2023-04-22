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
    
    if not(s1>e2 or e1<s2):
        overlaps += 1
print(overlaps)
    