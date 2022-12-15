import functools

def decode_line(line):
    output = []    
    pos = 0
    number = ''
       
    while pos<len(line)-1:
        char = line[pos]
        if char == '[':
            output.append([])
        elif char == ',':
            if number!='':
                output[-1].append(int(number))
                number = ''
        elif char == ']':
            if number!='':
                output[-1].append(int(number))
                number = ''
            l = output.pop(-1)
            output[-1].append(l)
        else:
            number += char   
        pos += 1
    if number!='':
        output[-1].append(int(number))
        number = ''
    
    return output[0]

def compare(a, b, correct=0):
    if correct == 0:
        if isinstance(a, int) and isinstance(b, int):
            return 0 if a==b else (a-b)/abs(a-b)
        elif isinstance(a, list) and isinstance(b, list):
            for i in range(len(a)):
                if i>=len(b):
                    correct = 1
                    break
                else:
                    correct = compare(a[i], b[i], correct)
                    if correct != 0:
                        break
            if correct == 0 and len(a)!=len(b):
                correct = -1
                
        else:
            if isinstance(a, int):
                a = [a]
            else:
                b = [b]
            correct = compare(a, b, correct)
    return correct

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

packets = [[[2]],[[6]]]
for line in lines:
    if line!='':
        c_packet = decode_line(line)
        packets.append(c_packet)

packets.sort(key=functools.cmp_to_key(compare))
first = 0
second = 0
for i in range(len(packets)):
    if packets[i] == [[2]]:
        first = i+1
    elif packets[i] == [[6]]:
        second = i+1
print(first*second)
        
        
        
        
        
        
        