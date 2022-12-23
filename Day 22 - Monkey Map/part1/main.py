def read_file(namefile):
    with open(namefile, 'r') as f:
        lines = f.read().splitlines()
    return lines

class Tile:
    def __init__(self, _x, _y, _data):
        self.x = _x
        self.y = _y
        self.data = _data

        # RIGHT=0 | DOWN=1 | LEFT=2 | UP=3      
        self.adjacent = [None, None, None, None]
     
    def set_right(self, tile):
        tile.set_left(self)
        
    def set_left(self, tile):
        self.adjacent[2] = tile
        tile.adjacent[0] = self
    
    def set_down(self, tile):
        tile.set_up(self)
    
    def set_up(self, tile):
        self.adjacent[3] = tile
        tile.adjacent[1] = self
    
    def __str__(self):
        string = ""
        string += str(self.x+1) + " " + str(self.y+1) + ": " + self.data
        return string

class Map_Manager:
    def __init__(self, day_input):
        self.start = None
        # READ MAP
        n_line = 0
        max_x = 0
        while(day_input[n_line]!=''):
            if len(day_input[n_line])>max_x:
                max_x = len(day_input[n_line])
            n_line += 1
        map_lines = day_input[:n_line]
        self.create_map(map_lines, max_x)
        # READ PATH
        n_line +=1
        self.path = day_input[n_line]
        self.navigate()
    
    def move(self, start, number, direction):
        for _ in range(number):
            n_tile = start.adjacent[direction]
            if n_tile.data == '#':
                break
            start = n_tile
        return start
    
    def navigate(self):
        c_tile = self.start
        print(c_tile)
        c_dirt = 0
        
        number = ""
        for char in self.path:
            if '0' <= char <= '9':
                number += char
                continue
            # MOVE
            number = int(number)  
            c_tile = self.move(c_tile, number, c_dirt)
            print(c_tile)
            number = ""
            # CHANGE DIRECTION
            if char == 'R':
                c_dirt += 1
            else:
                c_dirt -= 1
            c_dirt = c_dirt%4
        number = int(number)
        c_tile = self.move(c_tile, number, c_dirt)
    
        result = 1000*(c_tile.y+1) + 4*(c_tile.x+1) + c_dirt
        print(result)
        
    def create_map(self, lines, max_x):
        # READ MAP
        c_map = []
        for idx_y, c_line in enumerate(lines):
            c_row = []
            for idx_x, data in enumerate(c_line):
                if data == ' ':
                    c_row.append(None)
                    continue
                new_tile = Tile(idx_x, idx_y, data)
                c_row.append(new_tile)
                if not self.start:
                    self.start = new_tile
            c_row += [None]*(max_x - len(c_row))
            c_map.append(c_row)
        self.configure_map(c_map)
        
    def configure_map(self, c_map):
        # PRINT MAP
        for row in c_map:
            string = ""
            for element in row:
                if not element:
                    string += " "
                    continue
                string += element.data
            print(string)
        # CONFIGURE MAP
        u_end = [None]*len(c_map[0])
        u_previous = [None]*len(c_map[0])
        for row in c_map:
            l_previous = l_end = None
            for x, tile in enumerate(row):                
                if tile != None:
                    if l_previous == None:
                        l_end = tile
                    else:
                        tile.set_left(l_previous)
                 
                    if u_previous[x] == None:
                        u_end[x] = tile
                    else:
                        tile.set_up(u_previous[x])
                else:
                    if l_end != None:
                        l_end.set_left(l_previous)
                        l_end = None
                    if u_end[x]!=None:
                        u_end[x].set_up(u_previous[x])
                        u_end[x] = None
                l_previous = tile
            if l_end != None:
                l_end.set_left(l_previous)
            u_previous = row
        for x, end in enumerate(u_end):
            if end != None:
                end.set_up(u_previous[x])
                    
                    

  
if __name__ == "__main__":
    day_input = read_file("input.txt")
    
    manager = Map_Manager(day_input)  
    

        
        
        
         
    
    
