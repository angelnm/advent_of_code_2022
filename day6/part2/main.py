with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

for signal in lines:
    len_marker=14
    for i in range(len(signal)-len_marker+1):
        c_marker = signal[i:i+len_marker]
        if len(c_marker)==len(set(c_marker)):
            print(i+len_marker)
            break
        