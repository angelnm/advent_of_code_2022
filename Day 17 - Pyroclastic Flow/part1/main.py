def read_file(namefile):
    with open(namefile, 'r') as f:
        lines = f.read().splitlines()
    return lines

def read_jet_pattern(n, pattern):
    if pattern[n] == '>':
        return (n+1)%len(pattern), +1, 
    return (n+1)%len(pattern), -1
        
class Tower:
    def __init__(self, n=7):
        self.tower = []
        self.add_empty_lines(n)
     
    def add_empty_lines(self, n):
        for _ in range(n):
            self.tower.append(['.']*7)
    
    def get_max_height(self):
        for i in reversed(range(len(self.tower))):
            if self.tower[i] != ['.']*7:
                return i+1
        return 0
    
    def place_rock(self, rock):
        rock_x, rock_y = rock.center
        for rock_part in rock.rocks:
            self.tower[rock_y+rock_part[1]][rock_x+rock_part[0]] = '#'
        
        height = self.get_max_height()
        self.add_empty_lines(height+7-len(self.tower))
    
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
            if tower.tower[rock_y][rock_x]=='#':
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
            if tower.tower[rock_y][rock_x]=='#':
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
if __name__ == "__main__":
    jet_pattern = read_file("input.txt")[0]
    
    tower = Tower()
    print(tower)
    pattern_pos = 0
    start = time.time()
    for n in range(20000):
        height = tower.get_max_height()+3        
        
        rock = Rock(n, height)
        placed = False
        while not placed:
            pattern_pos, direction = read_jet_pattern(pattern_pos, jet_pattern)
            rock.horizontal_move(direction, tower)
            placed = rock.vertical_move(tower)
            if placed:
                tower.place_rock(rock)
    print(time.time()-start)
    print(tower.get_max_height())

         
    
    
