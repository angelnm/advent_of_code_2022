with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

head = [0,0]
tail = [0,0]
visited = {0:{0:True}}
dict_direction = {'R':[1,0], 'L':[-1,0], 'U':[0,1], 'D':[0, -1]}
for data in lines:
    direction, count = data.split()
    direction = dict_direction[direction]
    
    for _ in range(int(count)):
        # Move Head
        head[0] += direction[0]
        head[1] += direction[1]
        # Move Tail
        diff_x = head[0]-tail[0]
        diff_y = head[1]-tail[1]   
        if abs(diff_x) >=2 or abs(diff_y)>=2:
            tail[0] = tail[0] + diff_x/abs(diff_x) if diff_x!=0 else tail[0]
            tail[1] = tail[1] + diff_y/abs(diff_y) if diff_y!=0 else tail[1]
            
            if tail[0] not in visited:
                visited[tail[0]] = {}
            visited[tail[0]][tail[1]] = True

total_visited = 0
for x in visited:
    for y in visited[x]:
        total_visited += 1
print(total_visited)