with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

tree_map = []
visible = []
for line in lines:
    c_row = []
    c_vis = []
    for i in line:
        c_row.append(int(i))
        c_vis.append(False)
    tree_map.append(c_row)
    visible.append(c_vis)

h = len(tree_map)
w = len(tree_map[0])
# HORIZONTAL
for i in range(h):
    # IZQUIERDA->DERECHA
    height = -1
    for j in range(w):
        c_height = tree_map[i][j] 
        if c_height > height:
            height = c_height
            visible[i][j] = True
        if c_height == 9:
            break
    #DERECHA->IZQUIERDA    
    height = -1
    for j in reversed(range(w)):
        c_height = tree_map[i][j] 
        if c_height > height:
            height = c_height
            visible[i][j] = True
        if c_height == 9:
            break
 
# VERTICAL
for j in range(w):
    # ARRIBA->ABAJO
    height = -1
    for i in range(h):
        c_height = tree_map[i][j] 
        if c_height > height:
            height = c_height
            visible[i][j] = True
        if c_height == 9:
            break
    # ABAJO->ARRIBA
    height = -1
    for i in reversed(range(h)):
        c_height = tree_map[i][j] 
        if c_height > height:
            height = c_height
            visible[i][j] = True
        if c_height == 9:
            break
      
for visible_row in visible:
    string = ''
    for el in visible_row:
        if el:
            string += 'O '
        else:
            string += '  '
    print(string)
    
total_visible = 0
for visible_row in visible:
    for visible_cell in visible_row:
        if visible_cell:
            total_visible+=1
print(total_visible)