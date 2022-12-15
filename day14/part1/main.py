with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

min_x = 1000
max_x = 0
max_y = 0
paths = []
for line in lines:
    coordinates = line.split('->')
    c_path = []
    for c_coordinate in coordinates:
        x, y = c_coordinate.split(',')   
        x = int(x)
        y = int(y)
        c_path.append([x, y])
         
        min_x = min_x if min_x<x else x
        max_x = max_x if max_x>x else x
        max_y = max_y if max_y>y else y
    paths.append(c_path)   
min_x = min_x
max_x = max_x+1

cave_map = []
for i in range(max_y+1):
    c_row = ['.'] * (max_x - min_x)
    cave_map.append(c_row)

for path in paths:
    for i in range(len(path)-1):
        c_coor = path[i]
        n_coor = path[i+1]
        
        x_from = min(c_coor[0], n_coor[0])
        x_to   = max(c_coor[0], n_coor[0])
        y_from = min(c_coor[1], n_coor[1])
        y_to   = max(c_coor[1], n_coor[1])
        for x in range(x_from, x_to+1):
            for y in range(y_from, y_to+1):
                cave_map[y][x-min_x] = '#'

nonStop = True
n_sand = 0      
while(nonStop):
    # Spawn Arena
    c_coor = [500-min_x, 0]
    
    while(True):
        if c_coor[1]+1 >= len(cave_map):
            nonStop = False
            break
        elif cave_map[c_coor[1]+1][c_coor[0]] == '.':
            c_coor[1] +=1
        elif c_coor[0]-1<0:
             nonStop = False
             break
        elif cave_map[c_coor[1]+1][c_coor[0]-1] == '.':
            c_coor[0] -= 1
            c_coor[1] += 1
        elif c_coor[0]+1>=len(cave_map[0]):
            nonStop = False
            break
        elif cave_map[c_coor[1]+1][c_coor[0]+1] == '.':
            c_coor[0] += 1
            c_coor[1] += 1
        else:
            cave_map[c_coor[1]][c_coor[0]] = 'o'
            n_sand += 1
            break
print(n_sand)               

#for i in range(len(cave_map)):
#    print(i, cave_map[i])
