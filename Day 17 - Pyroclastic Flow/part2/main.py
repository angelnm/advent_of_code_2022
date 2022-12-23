def read_file(namefile):
    with open(namefile, 'r') as f:
        lines = f.read().splitlines()
    return lines

def read_jet_pattern(n, pattern):
    if pattern[n] == '>':
        return (n+1)%len(pattern), +1, 
    return (n+1)%len(pattern), -1
        
class Tower:
    def __init__(self, _pattern, n=7):
        self.tower = []
        self.add_empty_lines(n)
        
        self.min_height = 0
        self.pattern_pos = 0
        self.pattern = _pattern
     
    def add_empty_lines(self, n):
        for _ in range(n):
            self.tower.append(['.']*7)
    
    def get_max_height(self):
        for i in reversed(range(len(self.tower))):
            if self.tower[i] != ['.']*7:
                return i+1+self.min_height
        return self.min_height

    def check_pos(self, _x, _y, tag):
        if self.tower[_y-self.min_height][_x] == tag:
            return True
        return False
    
    def prune_tower(self):
        for i in reversed(range(len(self.tower))):
            row = self.tower[i]
            if not '.' in row:
                self.tower = self.tower[i:]
                self.min_height += i
                break
    
    def perform_n_iterations_pattern(self, n_iterations, x=1, iteration_offset=0):
        rock_positions = []
        start_pattern = -1
        size_pattern = -1
        
        for n in range(n_iterations):           
            n += iteration_offset
            height = self.get_max_height()+3
            
            rock = Rock(n, height)
            placed = False
            while not placed:
                self.pattern_pos, direction = read_jet_pattern(self.pattern_pos, self.pattern)
                rock.horizontal_move(direction, tower)
                placed = rock.vertical_move(self)
                if placed:
                    position = self.place_rock(rock) + [height-3]

                    if n%x==0:
                        print(len(rock_positions), size_pattern)
                        # Skip First Element                    
                        if len(rock_positions)<2:
                            rock_positions.append(position)
                            continue                    
                        # 1º Continue Pattern
                        if (start_pattern != -1 and
                            # Horizontal Check
                            position[0] == rock_positions[size_pattern+1][0] and
                            # Vertical Check
                            (size_pattern<1 or
                             rock_positions[size_pattern+1][1] - rock_positions[size_pattern][1] == position[1] - rock_positions[-1][1]
                             )):
                            size_pattern += 1
                        # 2º Start New Pattern
                        elif (position[0] == rock_positions[0][0]):
                            size_pattern = 0
                            start_pattern = len(rock_positions)
                        # 3º Not Continue or Start
                        else:
                            start_pattern = -1
                            size_pattern = -1
                            
                        if size_pattern!=-1 and size_pattern == start_pattern:
                            start_height = rock_positions[0][2]
                            end_height = rock_positions[start_pattern][2]
                            diff_height = end_height-start_height
                            
                            size_pattern *= x
                            a = (n_iterations//size_pattern) * diff_height
                            b = (n_iterations)%size_pattern
                            print(size_pattern, b)
                            print(start_height, end_height, diff_height)
                            print(start_height + a)
    
                            return start_height+a, b
                                            
                        rock_positions.append(position)
    
    def perform_n_iterations(self, n_iterations, iteration_offset=0):
        start_height = self.get_max_height()        
        for n in range(n_iterations):
            n += iteration_offset
            height = self.get_max_height()+3        
        
            rock = Rock(n, height)
            placed = False
            while not placed:
                self.pattern_pos, direction = read_jet_pattern(self.pattern_pos, self.pattern)
                rock.horizontal_move(direction, self)
                placed = rock.vertical_move(self)
                if placed:
                    self.place_rock(rock)
        return self.get_max_height() - start_height
    
    def place_rock(self, rock):
        rock_x, rock_y = rock.center
        rock_y -= self.min_height
        for rock_part in rock.rocks:
            self.tower[rock_y+rock_part[1]][rock_x+rock_part[0]] = '#'
        
        height = self.get_max_height()
        self.add_empty_lines(height+7-(len(self.tower)+self.min_height))
        
        tower.prune_tower()
        return [rock_x, rock_y+self.min_height]
    
    def __str__(self):
        string = ''
        for row in reversed(self.tower):
            for element in row:
                string += element
            string += '\n'
        return string 

class Rock:
    def __init__(self, _n, _height):
        self.center, self.rocks = self.get_rock_shape(_n, _height)
    
    def horizontal_move(self, direction, tower):
        new_x = self.center[0]+direction
        if new_x<0 or new_x>=7:
            return
        for rock in self.rocks:
            rock_x = rock[0]+new_x
            rock_y = rock[1]+self.center[1]
            if rock_x >=7:
                return
            if tower.check_pos(rock_x, rock_y,'#'):
                return
        self.center[0] = new_x
    
    def vertical_move(self, tower):
        new_y = self.center[1]-1
        if new_y<0:
            return True
        for rock in self.rocks:
            rock_x = rock[0]+self.center[0]
            rock_y = rock[1]+new_y
            if new_y<0:
                return True
            if tower.check_pos(rock_x, rock_y,'#'):
                return True
        self.center[1] = new_y
        return False
    
    def get_rock_shape(self, n, height):
        shape = n%5
        if shape==0:
            return [2, height], [ [0,0], [1,0], [2,0], [3,0] ]
        elif shape==1:
            return [2, height], [ [1,0], [0,1], [1,1], [2,1], [1,2] ]
        elif shape==2:
            return [2, height], [ [0,0], [1,0], [2,0], [2,1], [2,2] ]
        elif shape==3:
            return [2, height], [ [0,0], [0,1], [0,2], [0,3] ]
        else:
            return [2, height], [ [0,0], [0,1], [1,0], [1,1] ]

import time 
import copy   
if __name__ == "__main__":
    jet_pattern = read_file("input.txt")[0]
    
    tower = Tower(jet_pattern)
    n_ite = 1000000000000
    
    print(tower)
    print(len(jet_pattern))

    start = time.time()
    
    
    n = min(n_ite, len(jet_pattern)*5)
    tower.perform_n_iterations(n)
    print("First Phase Performed")
    n = n_ite-n
    if n>0:
        tmp = copy.deepcopy(tower)
        height, left_n = tower.perform_n_iterations_pattern(n, len(jet_pattern))
        print(tower.min_height)
        print(left_n)
        height += tmp.perform_n_iterations(left_n)
        print(height)
    else:
        print(tower.min_height)
        print(tower.get_max_height())
    print(time.time()-start)

         
    
    
