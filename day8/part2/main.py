tree_map = []
visible = []

def horizontal_loop(row, c_loop):
    dist = [1]*10
    for j in c_loop:
        c_height = tree_map[row][j]
        visible[row][j]*=dist[c_height]
        
        dist = [x+1 for x in dist]
        dist[:c_height+1] = [1]*(c_height+1)

def vertical_loop(column, c_loop):
    dist = [1]*10
    for i in c_loop:
        c_height = tree_map[i][column] 
        visible[i][column]*=dist[c_height]
            
        dist = [x+1 for x in dist]
        dist[:c_height+1] = [1]*(c_height+1)

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()    
    
    for line in lines:
        c_row = []
        c_vis = []
        for i in line:
            c_row.append(int(i))
            c_vis.append(1)
        tree_map.append(c_row)
        visible.append(c_vis)
    
    h = len(tree_map)
    w = len(tree_map[0])
    
    # HORIZONTAL
    for i in range(len(tree_map)):
        horizontal_loop(i, range(1,w))  
        horizontal_loop(i, reversed(range(0,w-1)))
         
    # VERTICAL
    for j in range(w):  
        vertical_loop(j, range(1,h))
        vertical_loop(j, reversed(range(0,h-1)))
    
    # DRAW MAP      
    for visible_row in visible:
        string = ''
        for el in visible_row:
            string += str(el) + ' '
        print(string)
    
    # GET_MAX
    max_value = 0
    for row in visible:
        for el in row:
            if el > max_value:
                max_value = el
    print(max_value)


main()