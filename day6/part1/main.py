with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

for signal in lines:
    for i in range(len(signal)-3):
        c_marker = signal[i:i+4]
        if len(c_marker)==len(set(c_marker)):
            print(i+4)
            break
        