def read_file(namefile):
    with open(namefile, 'r') as f:
        lines = f.read().splitlines()
    return lines

class Elf:
	def __init__(self, _x, _y):
		self.x = _x
		self.y = _y

	def __str__(self):
		string = ""
		string += str(self.x) + " " + str(self.y)
		return string

class Map_Manager:
	def __init__(self, day_input):
		self.elfs = {}
		for idx_y, row in enumerate(day_input):
			for idx_x, element in enumerate(row):
				if element == '.':
					continue
				new_elf = Elf(idx_x, idx_y)
				self.add_elf(new_elf, idx_x, idx_y)
		self.update_limits()
		self.check_dir = [NORTH, SOUTH, WEST, EAST]

	def update_limits(self):
		ys = sorted(self.elfs.keys())
		self.min_y = ys[0]
		self.max_y = ys[-1]

		self.min_x = 9999999
		self.max_x = -9999999
		for row_y in self.elfs.values():
			xs = sorted(row_y)
			self.min_x = min(xs[0], self.min_x)
			self.max_x = max(xs[-1], self.max_x)

	def update_direction(self):
		direction = self.check_dir.pop(0)
		self.check_dir.append(direction)

	def get_check_position(self, x, y):
		positions = []
		for direction in self.check_dir:
			if direction==NORTH or direction==SOUTH:
				c_x = [x, x+1, x-1]
				if direction==NORTH:
					c_y = [y-1]
				else:
					c_y = [y+1]
			else:
				c_y = [y, y-1, y+1]
				if direction==EAST:
					c_x = [x+1]
				else:
					c_x = [x-1]
			positions.append([c_x, c_y, direction])
		return positions

	def any_elf(self, x, y):
		if y in self.elfs:
			if x in self.elfs[y]:
				return True
		return False

	def is_occupied(self, positions):
		for x, y in positions:
			if self.any_elf(x, y):
				return True
		return False

	def check_elf(self, elf):
		movement = -1
		empty = True
		for dir_x, dir_y, direction in self.get_check_position(elf.x, elf.y):			
			positions = []
			for x in dir_x:
				for y in dir_y:
					positions.append([x, y])

			occupied = self.is_occupied(positions)
			if occupied:
				empty = False
				continue
			if movement == -1:			
				movement = [dir_x[0], dir_y[0], direction]

		if empty or movement==-1:
			return elf.x, elf.y, NONE
		return movement

	def add_elf(self, elf, x, y):
		if y not in self.elfs:
			self.elfs[y] = {}
		self.elfs[y][x] = elf
		elf.x = x
		elf.y = y

	def move_elf(self, elf, x, y, direction):
		if direction == NONE:
			return
		del self.elfs[elf.y][elf.x]
		if self.elfs[elf.y] == {}:
			del self.elfs[elf.y]
		self.add_elf(elf, x, y)

	def perform_round(self):
		proposed = {}
		for row_y in self.elfs.values():
			for c_elf in row_y.values():
				new_x, new_y, direction = self.check_elf(c_elf)
				if direction == NONE:
					continue

				if new_y not in proposed:
					proposed[new_y] = {}
				if new_x not in proposed[new_y]:
					proposed[new_y][new_x] = []
				proposed[new_y][new_x].append([c_elf, direction])
		
		movement = False
		for y in proposed:
			for x in proposed[y]:
				pro = proposed[y][x]
				if len(pro) != 1:
					continue
				movement = True
				elf, direction = pro[0]
				self.move_elf(elf, x, y, direction)
		self.update_direction()
		self.update_limits()
		return movement

	def get_area(self):
		area = (self.max_x+1-self.min_x)
		area *= (self.max_y+1-self.min_y)

		return area

	def get_total_elfs(self):
		n_elfs = 0
		for row_y in self.elfs.values():
			n_elfs += len(row_y)
		return n_elfs

	def __str__(self):
		string = ""
		for y in range(self.min_y, self.max_y+1,1):
			if y not in self.elfs:
				string += '.'*(self.max_x-self.min_x)
				string += '\n'
				continue
			previous_x = self.min_x
			for x in sorted(self.elfs[y]):
				string += '.'*(x-previous_x)
				string += '#'
				previous_x = x+1
			string += '.'*(self.max_x+1-previous_x)
			string += '\n'
		return string
  
NONE =-1  
NORTH=0
EAST =1
SOUTH=2
WEST =3
if __name__ == "__main__":
    day_input = read_file("input.txt")
    
    manager = Map_Manager(day_input)

    n_ite = 0
    movement = True
    while movement:
    	movement = manager.perform_round()
    	n_ite += 1
    print(manager)
    print(n_ite)
    

        
        
        
         
    
    
