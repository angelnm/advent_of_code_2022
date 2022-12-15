with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

# Read Stacks
stack=[]
for line in lines:
    if line[0:4]!='move':
         for i in range(0,(len(line)+1)//4):
             c_char = line[i*4+1]
             if c_char != ' ' and not ('1'<=c_char<='9'):
                 while len(stack)<i+1:
                     stack.append([])
                 stack[i].insert(0,c_char)
    else:
        ele = line.split()
        total = int(ele[1])
        c_fr = int(ele[3])-1
        c_to = int(ele[5])-1
        for i in range(total):
            crate = stack[c_fr].pop()
            stack[c_to].append(crate)

result = ''
for pile in stack:
    result += pile[-1]
print(result)