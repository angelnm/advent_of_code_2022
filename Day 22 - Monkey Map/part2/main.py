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
    
    def get_right(self):
        return self.adjacent[0]
    def get_down(self):
        return self.adjacent[1]
    def get_left(self):
        return self.adjacent[2]
    def get_up(self):
        return self.adjacent[3]
    
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

class Cube:
    def __init__(self, _id, _start):
        self.id = _id
        self.start = _start
        
        # RIGHT=0 | DOWN=1 | LEFT=2 | UP=3
        self.adjacent =  [None, None, None, None]
        self.connected = [False, False, False, False]
    
    def check_sides(self):
        #print("START", self)
        for side, cube_info in enumerate(self.adjacent):
            if cube_info == None:
                continue
            rot = cube_info[1]
            cube = cube_info[0]
            #print("\tCHECK", cube, rot)
            adjacent = cube.adjacent
            for n_side, n_cube in enumerate(adjacent):
                if n_cube == None:
                    continue
                n_side = (n_side+rot)%4
                if self.adjacent[n_side] == None and n_cube[0]!=self:
                    rot += (n_side - side) + n_cube[1]
                    rot = rot%4
                    #print("\t\tPUT", n_cube[0], "POS", n_side, "ROT", rot)
                    self.adjacent[n_side] = [n_cube[0], rot]
                    #print("\t\t", self)
        #print("END", self)
    
    def get_adjacent(self, cube):
        for idx, adj in enumerate(self.adjacent):
            if adj == None:
                continue
            if adj[0] == cube:
                return idx
        return -1
    
    def is_complet(self):
        for side in self.adjacent:
            if side == None:
                return False
        return True
    
    def get_up_row(self):
        tiles = [self.start]
        for _ in range(CUBE_SIZE-1):
            tiles.append(tiles[-1].get_right())
        return tiles
    def get_left_row(self):
        tiles = [self.start]
        for _ in range(CUBE_SIZE-1):
            tiles.append(tiles[-1].get_down())
    def get_down_row(self):
        start = self.start
        for _ in range(CUBE_SIZE-1):
            start = start.get_down()
        tiles = [start]
        for _ in range(CUBE_SIZE-1):
            tiles.append(tiles[-1].get_right())
        return tiles
    def get_right_row(self):
        start = self.start
        for _ in range(CUBE_SIZE-1):
            start = start.get_right()
        tiles = [start]
        for _ in range(CUBE_SIZE-1):
            tiles.append(tiles[-1].get_down())
        return tiles
    
    def set_right(self, cube):
        self.adjacent[0] = [cube, 0]
        self.connected[0] = True
    def set_down(self, cube, rot=0):
        self.adjacent[1] = [cube, 0]
        self.connected[1] = True
    def set_left(self, cube, rot=0):
        self.adjacent[2] = [cube, 0]
        self.connected[2] = True
    def set_up(self, cube, rot=0):
        self.adjacent[3] = [cube, 0]
        self.connected[3] = True
    
    def __str__(self):
        string = ""
        string += str(self.id) + " "
        string += "["
        for cube in self.adjacent:
            if cube == None:
                string += "_ "
                continue
            string += str(cube[0].id) + " "
        string += "]"
        return string

class Map_Manager:
    def __init__(self, day_input):
        self.start_tile = None
        self.start_cube = None
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
        #self.navigate()
    
    def move(self, start, number, direction):
        for _ in range(number):
            n_tile = start.adjacent[direction]
            if n_tile.data == '#':
                break
            start = n_tile
        return start
    
    def navigate(self):
        c_tile = self.start_tile
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
                if not self.start_tile:
                    self.start_tile = new_tile         
            c_row += [None]*(max_x - len(c_row))
            c_map.append(c_row)
        self.configure_map(c_map)   
        # READ CUBES
        c_cubes = []
        cube_id = 1
        for y in range(len(lines)//CUBE_SIZE):
            c_row = []
            for x in range(max_x//CUBE_SIZE):
                c_tile = c_map[y*CUBE_SIZE][x*CUBE_SIZE]
                if c_tile==None:
                    c_row.append(None)
                    continue
                new_cube = Cube(cube_id, c_tile)
                c_row.append(new_cube)
                if not self.start_cube:
                    self.start_cube = new_cube
                cube_id +=1               
            c_cubes.append(c_row)
        self.configure_cube(c_cubes)
        

    def configure_cube(self, c_cubes):
        # PRINT CUBE
        for row in c_cubes:
            string = ""
            for cube in row:
                if not cube:
                    string += " "
                    continue
                string += str(cube.id)
            print(string)
        # BASIC CONFIGURE
        cube_list = []
        for idx_y, row in enumerate(c_cubes):
            for idx_x, cube in enumerate(row):
                if cube == None:
                    continue
                cube_list.append(cube)
                if idx_x>0 and c_cubes[idx_y][idx_x-1]!=None:
                    cube.set_left(c_cubes[idx_y][idx_x-1])
                if idx_x<len(row)-1 and c_cubes[idx_y][idx_x+1]!=None:
                    cube.set_right(c_cubes[idx_y][idx_x+1])
                if idx_y>0 and c_cubes[idx_y-1][idx_x]!=None:
                    cube.set_up(c_cubes[idx_y-1][idx_x])
                if idx_y<len(c_cubes)-1 and c_cubes[idx_y+1][idx_x]!=None:
                    cube.set_down(c_cubes[idx_y+1][idx_x])
        # PRO CONFIGURE
        copy_list = []
        for c in cube_list:
            copy_list.append(c)
        while len(copy_list)>0: 
            c_cube = copy_list.pop(0)
            c_cube.check_sides()
            if not c_cube.is_complet():
                copy_list.append(c_cube)
        # CONECT TILES
        """
        for cube in cube_list:
            print(cube)
            for side, (n_cube, connected) in enumerate(zip(cube.adjacent, cube.connected)):
                if connected:
                    continue
                print(side, n_cube[0].get_adjacent(cube))
        """
                
        
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
        u_previous = [None]*len(c_map[0])
        for row in c_map:
            l_previous = None
            for x, tile in enumerate(row):                
                if tile != None:
                    if l_previous != None:
                        tile.set_left(l_previous)        
                    if u_previous[x] != None:
                        tile.set_up(u_previous[x])
                l_previous = tile
            u_previous = row
                    
                    

CUBE_SIZE = 4 
if __name__ == "__main__":
    day_input = read_file("input.txt")
    
    manager = Map_Manager(day_input)  
    

        
        
        
         
    
    
