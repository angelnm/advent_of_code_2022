with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

#head = [0,0]
#tail = [0,0]
num_elements = 10
    
rope = []
for elements in range(num_elements):
    rope.append([0,0])

visited = []
for elements in range(num_elements):
    visited.append({0:{0:True}})
def add_visited(c_id, c_position):
    c_dict = visited[c_id]
    if c_position[0] not in c_dict:
        c_dict[c_position[0]] = {}
    c_dict[c_position[0]][c_position[1]] = True

dict_direction = {'R':[1,0], 'L':[-1,0], 'U':[0,1], 'D':[0, -1]}
for data in lines:
    direction, count = data.split()
    direction = dict_direction[direction]
    
    for _ in range(int(count)):
        # Move Head
        c_cell = rope[0]
        c_cell[0] += direction[0]
        c_cell[1] += direction[1]
        add_visited(0, [c_cell[0],c_cell[1]])
        
        # Move Ropes
        for i in range(1, len(rope)):
            l_cell = rope[i-1]
            c_cell = rope[i]
            
            diff_x = l_cell[0]-c_cell[0]
            diff_y = l_cell[1]-c_cell[1]         
            if abs(diff_x) >=2 or abs(diff_y)>=2:
                c_cell[0] = c_cell[0] + diff_x/abs(diff_x) if diff_x!=0 else c_cell[0]
                c_cell[1] = c_cell[1] + diff_y/abs(diff_y) if diff_y!=0 else c_cell[1]
            
                add_visited(i, [c_cell[0], c_cell[1]])

rope_id = 9
total_visited = 0
for x in visited[rope_id]:
    for y in visited[rope_id][x]:
        total_visited += 1
print(total_visited)