with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

x = 1
cycle = 0
string = ''
for line in lines:
    string += '#' if cycle-1<=x<=cycle+1 else '.'
    
    if line[:4]=='noop':
        cycle = cycle+1 if cycle<39 else 0
    else:
        cycle = cycle+1 if cycle<39 else 0
        string += '#' if cycle-1<=x<=cycle+1 else '.'
        
        _, value = line.split()
        value = int(value)
        
        cycle = cycle+1 if cycle<39 else 0
        x += value

for i in range(0,220,40):
    print(string[i:i+40])
        
