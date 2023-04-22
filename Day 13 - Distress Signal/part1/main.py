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

def compare(a, b, correct=None):  
    if correct == None:
        if isinstance(a, int) and isinstance(b, int):
            return None if a==b else a<b
        elif isinstance(a, list) and isinstance(b, list):
            for i in range(len(a)):
                if i>=len(b):
                    correct = False
                    break
                else:
                    correct = compare(a[i], b[i], correct)
                    if correct != None:
                        break
            if correct == None and len(a)!=len(b):
                correct = True
                
        else:
            if isinstance(a, int):
                a = [a]
            else:
                b = [b]
            correct = compare(a, b, correct)
    return correct

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

total_sum = 0
pair = 1
for i in range(0, len(lines), 3):
    left  = decode_line(lines[i])
    right = decode_line(lines[i+1])

    correct = compare(left, right)
    if correct:
        total_sum += pair
    pair += 1
print(total_sum)