with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

start = []
end = [-1, -1] 

c_map = []
steps = []

# READ MAP
for i in range(len(lines)):
    c_row = []
    tmp_steps = []
    for j in range(len(lines[i])):
        char = lines[i][j]
        if char == 'S' or char=='a':
            char = 'a'
            start.append([i, j])
        elif char == 'E':
            char = 'z'
            end = [i, j]
        char = ord(char)-97
        c_row.append(char)
        tmp_steps.append(-1)
    c_map.append(c_row)
    steps.append(tmp_steps)

# MOVE
move_list = [s for s in start]
for move in move_list:
    steps[move[0]][move[1]] = 0
while len(move_list)>0:
    c_movement = move_list.pop(0)
    x = c_movement[0]
    y = c_movement[1]
    
    c_steps = steps[x][y]+1
    c_height = c_map[x][y]
    
    # UP
    if y>0 and c_map[x][y-1]<=c_height+1: 
        if (steps[x][y-1]==-1 or c_steps<steps[x][y-1]):
            move_list.append([x, y-1])
            steps[x][y-1] = c_steps
    # DOWN
    if y<len(c_map[0])-1 and c_map[x][y+1]<=c_height+1:
        if (steps[x][y+1]==-1 or c_steps<steps[x][y+1]):
            move_list.append([x, y+1])
            steps[x][y+1] = c_steps
    # LEFT
    if x>0 and c_map[x-1][y]<=c_height+1:
        if (steps[x-1][y]==-1 or c_steps<steps[x-1][y]):
            move_list.append([x-1, y])
            steps[x-1][y] = c_steps
    # RIGHT
    if x<len(c_map)-1 and c_map[x+1][y]<=c_height+1:
        if (steps[x+1][y]==-1 or c_steps<steps[x+1][y]):
            move_list.append([x+1, y])
            steps[x+1][y] = c_steps

# PRINT MAPS
for l in c_map:
    print(l)
print()
for l in steps:
    print(l)
print()
print(steps[end[0]][end[1]])
