def read_file(namefile):
    with open(namefile, 'r') as f:
        lines = f.read().splitlines()
    return lines

class Blizzard:
	def __init__(self, _x, _y, _tag):
		self.x = _x
		self.y = _y
		self.tag = _tag

		self.set_dir(self.tag)

	def get_position(self):
		return self.x, self.y

	def next_position(self):
		return self.x + self.dir[0], self.y + self.dir[1]

	def set_dir(self, _tag):
		if _tag == '^':
			self.dir = [0, -1]
		elif _tag == 'v':
			self.dir = [0, +1]
		elif _tag == '<':
			self.dir = [-1, 0]
		else:
			self.dir = [+1, 0]

class Player:
	def __init__(self, _start, _end):
		self.path = []
		self.end = _end
		self.beam_size = 100000

		self.init_path(_start)

	def init_path(self, start):
		new_path = []
		new_path.append(start)
		self.path.append(new_path)

	def has_end(self):
		for path in self.path:
			last_pos = path[-1]
			if last_pos[0] == self.end[0] and last_pos[1] == self.end[1]:
				return True
		return False

	def check_position(self, x, y, c_map):
		if x<0 or x>=len(c_map[0]):
			return False
		if y<0 or y>=len(c_map):
			return False
		if len(c_map[y][x])==0:
			return True
		return False

	def already_visited(self, x, y, positions):
		if y not in positions:
			return False
		if x not in positions[y]:
			return False
		return True

	def add_visited_position(self, x, y, positions):
		if y not in positions:
			positions[y] = []
		if x not in positions[y]:
			positions[y].append(x)

	def move(self, c_map):
		new_paths = []
		c_positions = {}
		for path in self.path:
			last_pos = path[-1]
			# DONT MOVE
			x, y = last_pos
			if self.check_position(x, y, c_map):
				if not self.already_visited(x, y, c_positions):
					self.add_visited_position(x, y, c_positions)
					new_paths.append(path+[[x, y]])
			# Move RIGHT
			x, y = last_pos
			x = x+1
			if self.check_position(x, y, c_map):
				if not self.already_visited(x, y, c_positions):
					self.add_visited_position(x, y, c_positions)
					new_paths.append(path+[[x, y]])
			# Move LEFT
			x, y = last_pos
			x = x-1
			if self.check_position(x, y, c_map):
				if not self.already_visited(x, y, c_positions):
					self.add_visited_position(x, y, c_positions)
					new_paths.append(path+[[x, y]])
			# Move UP
			x, y = last_pos
			y = y-1
			if self.check_position(x, y, c_map):
				if not self.already_visited(x, y, c_positions):
					self.add_visited_position(x, y, c_positions)
					new_paths.append(path+[[x, y]])
			# Move DOWN
			x, y = last_pos
			y = y+1
			if self.check_position(x, y, c_map):
				if not self.already_visited(x, y, c_positions):
					self.add_visited_position(x, y, c_positions)
					new_paths.append(path+[[x, y]])
		new_paths = sorted(new_paths, key=lambda x: self.score(x[-1]))
		total = 0
		for row in c_positions.values():
			total += len(row)
		self.path = new_paths[:self.beam_size]

	def score(self, position):
		a = pow(self.end[0] - position[0],2)
		b = pow(self.end[1] - position[1],2)
		return a+b

	def has_position(self, x, y):
		for path in self.path:
			last_position = path[-1]
			if last_position[0] == x and last_position[1] == y:
				return True
		return False

class Map_Manager:
	def __init__(self, day_input):
		self.map = []
		self.blizzards = []
		for y, row in enumerate(day_input):
			c_row = []
			for x, element in enumerate(row):
				if element == '#':
					c_row.append(element)
				elif element == '.':
					c_row.append([])
				else:
					new_blizzard = Blizzard(x, y, element)
					self.blizzards.append(new_blizzard)
					c_row.append([new_blizzard])
			self.map.append(c_row)
		
	def set_player(self, start, end):
		self.player = Player(start, end)

	def check_end(self):
		return self.player.has_end()

	def fix_position(self, x, y):
		if x<=0:
			x = len(self.map[0])-2
		elif x>=len(self.map[0])-1:
			x = 1

		if y<=0:
			y = len(self.map)-2
		elif y>=len(self.map)-1:
			y = 1

		return x, y

	def add_blizzard(self, blizzard, x, y):
		self.map[y][x].append(blizzard)
		blizzard.x = x
		blizzard.y = y

	def step(self):
		for c_blizzard in self.blizzards:
			x, y = c_blizzard.get_position()
			self.map[y][x].remove(c_blizzard)
			x, y = c_blizzard.next_position()
			x, y = self.fix_position(x, y)
			self.add_blizzard(c_blizzard, x, y)
		self.player.move(self.map)

	def __str__(self):
		string = ""
		for y, row in enumerate(self.map):
			for x, element in enumerate(row):
				if isinstance(element, str):
					string += element
				elif len(element)==0:
					string += '.'
				elif len(element)==1:
					string += element[0].tag
				else:
					string += str(len(element))
			string += '\n'

		for path in self.player.path:
			x, y = path[-1]
			pos = (len(self.map[0])+1)*y+x
			string = string[:pos] + 'E' + string[pos+1:]
		return string

if __name__ == "__main__":
	day_input = read_file("input.txt")
	
	manager = Map_Manager(day_input)
	start = [1,0]
	end   = [len(manager.map[0])-2, len(manager.map)-1]

	manager.set_player(start, end)
	cont = 0
	while not manager.check_end():
		print(cont, len(manager.player.path))
		print(manager)
		manager.step()
		cont += 1

	print(manager)
	print(cont)
