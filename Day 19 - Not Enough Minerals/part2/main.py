def read_file(namefile):
    with open(namefile, 'r') as f:
        lines = f.read().splitlines()
    return lines

class  State_Info:
    def __init__(self, _minute, _robots, _materials, _actions=[]):
        self.minute = _minute
        
        self.robots = _robots
        self.materials = _materials
        self.actions = _actions
    
    def add_action(self, action, _cost):
        n_action = self.copy()
        
        n_action.minute += 1
        n_action.actions += [action]
        
        n_action.add_materials()
        if action != -1:
            n_action.remove_materials(action, _cost)
            n_action.robots[action] += 1
        
        return n_action
    
    def add_materials(self):
        for idx, nb_robot in enumerate(self.robots):
            self.materials[idx] += nb_robot
        
    def remove_materials(self, action, _cost):
        c_cost = _cost[action]
        for idx, ore_cost in enumerate(c_cost):
            self.materials[idx] -= ore_cost
        
    def get_possible_action(self, _cost):
        action = [-1]
        for idx, c_cost in enumerate(_cost):
            if self.have_materials(c_cost):
                action.append(idx)
        return action
    
    def have_materials(self, _cost):
        for idx, c in enumerate(_cost):
            if self.materials[idx] < c:
                return False
        return True
    
    def score(self):
        score = 0
        time = MAX_TIME - self.minute
        for idx, mat in enumerate(self.materials):
            score += (mat + time*self.robots[idx])*ORE_WEIGHT[idx]
        return score
    
    def copy(self):
        _robots = []
        for r in self.robots:
            _robots.append(r)
        _materials = []
        for m in self.materials:
            _materials.append(m)
        _actions = []
        for a in self.actions:
            _actions.append(a)
        
        return State_Info(self.minute, _robots, _materials, _actions)
    
    def __str__(self):
        string = ""
        string += "Minute " + str(self.minute) + " -> "
        string += str(self.score()) + " -> "
        string += str(self.robots) + " "
        string += str(self.materials) + "\n\t"
        string += str(self.actions)
        return string

class Blueprint:
    def __init__(self, blueprint_input):
        bp_id, bp_info = blueprint_input.split(':')
        # Read ID
        _, bp_id = bp_id.split()
        bp_id = int(bp_id)
        # Read INFO
        bp_cost = [0]*len(ORE2POS)
        ores_info = bp_info.split('.')
        for idx, ore in enumerate(ores_info[:-1]):
            bp_cost[idx] = self.get_cost(ore)
        # Save INFO
        self.id = bp_id
        self.cost = bp_cost
        # Set START MATERIALS
        self.beam_size = 10000
        self.states = []
        self.states.append(State_Info(0, [1,0,0,0], [0,0,0,0], []))
        
    def compute_max_geodes(self):
        for _ in range(MAX_TIME):
            new_states = []
            for state in self.states:
                actions = state.get_possible_action(self.cost)
                for c_action in actions:
                    new_states.append(state.add_action(c_action, self.cost))
            self.states = sorted(new_states, key=lambda x: x.score(), reverse=True)[:self.beam_size]
       
        best_state = self.states[0]
        print(best_state)
        quality_level = self.id*best_state.materials[3]
        return best_state.materials[3]
     
    def get_cost(self, ore_info):
        cost = [0]*(len(ORE2POS)-1)
        
        ore_info = ore_info.split()
        for idx, el in enumerate(ore_info):
            if '0' <= el[0] <= '9':
                el = int(el)
                ore = ORE2POS[ore_info[idx+1]]
                cost[ore] = el     
        return cost
    
    def __str__(self):
        string = ""
        string += "ID " + str(self.id) + ": "
        for ore_cost in self.cost:
            string += str(ore_cost) + " "
        return string

ORE2POS = {'ore':0, 'clay':1, 'obsidian':2, 'geode':3}
n=1000
ORE_WEIGHT = [pow(n,x) for x in range(4)]
MAX_TIME=32      
if __name__ == "__main__":
    day_input = read_file("input.txt")
    
    total_mult = 1
    for blueprint_input in day_input[:3]:
        bp = Blueprint(blueprint_input)
        print(bp)
        total_mult *= bp.compute_max_geodes()
        print()
    print(total_mult)
        
        
        
         
    
    
