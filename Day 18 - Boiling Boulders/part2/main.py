def read_file(namefile):
    with open(namefile, 'r') as f:
        lines = f.read().splitlines()
    return lines

class Cube:
    def __init__(self, cube_str):
        x, y, z = cube_str.split(',')
        
        self.pos = [int(x), int(y), int(z)]
        self.sum_pos = sum(self.pos)
        
        self.surface = 6
        self.surface_edge = [[1,1],[1,1],[1,1]]

    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]
    
    def get_z(self):
        return self.pos[2]

    def adjacent(self, cube, edge):
        diff = cube.pos[edge] - self.pos[edge]
        if diff == -1:
            self.surface_edge[edge][0] = 0
            cube.surface_edge[edge][1] = 0
        elif diff == 1:
            self.surface_edge[edge][1] = 0
            cube.surface_edge[edge][0] = 0
            
    def compare_adjacent(self, cube):
        if self.surface == 0:
            return
        
        equal_pos = 0
        equal_pos += 100 if self.pos[0] == cube.pos[0] else 000
        equal_pos += 10 if self.pos[1] == cube.pos[1] else 000
        equal_pos += 1 if self.pos[2] == cube.pos[2] else 000
        
        if equal_pos == 0 or equal_pos == 100 or equal_pos == 10 or equal_pos == 1:
            return
        if abs(self.sum_pos - cube.sum_pos)>1:
            return
        
        if equal_pos == 11:
            self.adjacent(cube, 0)
        elif equal_pos == 101:
            self.adjacent(cube, 1)
        elif equal_pos == 110:
            self.adjacent(cube, 2)
        
        self.surface -= 1
        cube.surface -= 1
    
    def __str__(self):
        return "#"
        string = ""
        string += str(self.pos) + ": "
        string += str(self.surface)
        return string

class Obsidian:
    def __init__(self):
        self.cubes = []
        
        self.matrix = []
        self.start_pos = [0,0,0]

    def add_cube_input(self, cube_input):
        max_x = max_y = max_z = 0
        min_x = min_y = min_z = 999999
        for cube in cube_input:
            new_cube = Cube(cube)
            self.add_cube(new_cube)
            
            max_x = max(max_x, new_cube.get_x()+1)
            min_x = min(min_x, new_cube.get_x()-1)
            max_y = max(max_y, new_cube.get_y()+1)
            min_y = min(min_y, new_cube.get_y()-1)
            max_z = max(max_z, new_cube.get_z()+1)
            min_z = min(min_z, new_cube.get_z()-1)
        self.start_pos = [min_x, min_y, min_z]
        self.create_matrix(self.start_pos, [max_x, max_y, max_z])
        self.compute_surface()
        
    def create_matrix(self, min_pos, max_pos):
        self.matrix = []
        for x in range(min_pos[0], max_pos[0]+1):
            current_x = []
            for y in range(min_pos[1], max_pos[1]+1):
                current_y = []
                for z in range(min_pos[2], max_pos[2]+1):
                    current_y.append('·')
                current_x.append(current_y)
            self.matrix.append(current_x)
            
        for cube in self.cubes:
            x, y, z = cube.pos
            x -= self.start_pos[0]
            y -= self.start_pos[1]
            z -= self.start_pos[2]
            self.matrix[x][y][z] = cube

    def add_cube(self, new_cube):
        self.cubes.append(new_cube)
        
    def compute_surface(self):
        for i in range(len(self.cubes)):
            c_cube = self.cubes[i]
            for cube in self.cubes[i+1:]:
                c_cube.compare_adjacent(cube)
        
    def get_exterior_surface(self):
        surface = 0
        coord_list = [[0,0,0]]
        self.matrix[0][0][0] = 'o'
        
        while coord_list:
            c_coord = coord_list.pop()
            x, y, z = c_coord
            
            new_coords = []
            for new_x in [-1, +1]:
                c_x = x+new_x
                if c_x<0 or c_x>=len(self.matrix):
                    continue
                new_coords.append([c_x, y, z])
            for new_y in [-1, +1]:
                c_y = y+new_y
                if c_y<0 or c_y>=len(self.matrix[0]):
                    continue
                new_coords.append([x, c_y, z])
            for new_z in [-1, +1]:
                c_z = z+new_z
                if c_z<0 or c_z>=len(self.matrix[0][0]):
                    continue
                new_coords.append([x, y, c_z])
              
            for coord in new_coords:
                c_x, c_y, c_z = coord
                el = self.matrix[c_x][c_y][c_z]
                if  el == '·':
                    self.matrix[c_x][c_y][c_z] = 'o'
                    coord_list.append(coord)
                elif isinstance(el, Cube):
                    surface += 1
        return surface
                
                       
    def get_surface(self):
        total_sum = 0
        for cube in self.cubes:
            total_sum += cube.surface
        return total_sum
    
    def get_size_matrix(self):
        return [len(self.matrix),len(self.matrix[0]),len(self.matrix[0][0])]
        
    def print_matrix(self):
        for idx, row_x in enumerate(self.matrix):
            string = str(idx+self.start_pos[0]) + "\n"
            for row_y in row_x:
                for row_z in row_y:
                    string += str(row_z)
                string += "\n"
            print(string)
            
import time    
if __name__ == "__main__":
    day_input = read_file("input.txt")
    
    start = time.time()
    obsidian = Obsidian()
    obsidian.add_cube_input(day_input)
    
    exterior_surface = obsidian.get_exterior_surface()
    #print(obsidian.print_matrix())
    print(exterior_surface)
    print(obsidian.get_surface())
    print(time.time()-start)
        
        
         
    
    
