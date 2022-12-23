def read_file(namefile):
    with open(namefile, 'r') as f:
        lines = f.read().splitlines()
    return lines

def get_graph_rewards(graph, start, time):
    rewards = {}
    to_compute = [[start, time-1]]
    while(to_compute != []):
        c_node, time = to_compute.pop()
        c_reward = c_node.rate*(time)
        rewards[c_node.name]= [c_reward, time]   
        
        time = time-1
        if time>0:
            for connection in c_node.connections:
                c_child = graph[connection]
                if (c_child.name not in rewards or 
                c_child.rate*(time)>rewards[c_child.name][0]):
                    to_compute.append([c_child, time])
        to_compute = sorted(to_compute, key=lambda x: x[1], reverse=False)
    
    return rewards

def get_max_reward(reward, path, beam_size):
    valve_data = []
    
    for valve in reward:
        if valve not in path:
            valve_data.append([valve] + reward[valve])
    
    valve_data = sorted(valve_data, key=lambda x: x[1], reverse=True)   
    return valve_data[:beam_size]

class Node:
    def __init__(self, _name, _rate, _connections):
        self.name = _name
        self.rate = _rate
        self.connections = _connections
    
    def __str__(self):
        string = "Valve {0} with rate={1}; Lead to ".format(self.name, self.rate)
        for connection in self.connections:
            string += connection + " "
        return string

class Path_Information:
    def __init__(self, _time, _pressure, _post=['AA','AA'], _path=[]):
        self.you_time = _time[0]
        self.you_post = _post[0]
        self.ele_time = _time[1]
        self.ele_post = _post[1]
        
        self.pressure = _pressure
        self.path = _path
    
    def update(self, _tag, _time, _pressure, _post):
        self.pressure += _pressure
        if _tag == 'you':
            self.update_you(_time, _post)
            return
        self.update_ele(_time, _post)
    
    def update_you(self, _time, _post):
        self.you_time = _time
        self.you_post = _post

        
    def update_ele(self, _time, _post):
        self.ele_time = _time
        self.ele_post = _post
    
    def get_score(self):
        return self.pressure
        
    def __str__(self):
        string = str(self.pressure) + " " + str(26-self.time) + " " + str(self.path)
        return string
import copy
if __name__ == "__main__":
    day_input = read_file("input.txt")

    valves = {}
    for valve_scan in day_input:
        flow_rate, tunnels = valve_scan.split(';')
        
        flow_rate = flow_rate.split()
        name = flow_rate[1]
        rate = int(flow_rate[4].split('=')[1])
        
        c_connections = []
        for connection in tunnels[23:].split(','):
            connection = connection.replace(' ','')
            c_connections.append(connection)
            
        c_node = Node(name, rate, c_connections)
        valves[name] = c_node
    
    beam_size = 200000
    
    path_info = []
    best = None
    path_info.append(Path_Information([26, 26], 0))
    
    i = 0
    while i<len(valves):
        new_path_info = []
        for info in path_info:
            you_start = info.you_post
            ele_start = info.ele_post
            
            you_reward = get_graph_rewards(valves, valves[you_start], info.you_time)
            ele_reward = get_graph_rewards(valves, valves[ele_start], info.ele_time)
            
            you_valve_data = [ x + ['you'] for x in get_max_reward(you_reward, info.path, beam_size)]
            ele_valve_data = [ x + ['ele'] for x in get_max_reward(ele_reward, info.path, beam_size)]
            combined_data = sorted(you_valve_data + ele_valve_data, key=lambda x: x[1], reverse=True)[:beam_size]
            
            if not best or info.pressure > best.pressure:
                new_info = copy.deepcopy(info)
                best = new_info
            for data in combined_data:
                if data[1] != 0:
                    new_info = copy.deepcopy(info)
                    new_info.update(data[3], data[2], data[1], data[0])
                    new_info.path.append(data[0])
                    new_path_info.append(new_info)
        
        path_info = sorted(new_path_info, key=lambda x: x.get_score(), reverse=True)[:beam_size]
        i += 1


    print(best.pressure, best.you_time, best.ele_time)
    print(best.path)
    for info in path_info[:2]:
        print(info.pressure, info.you_time, info.ele_time)
        print(info.path)
         
    
    
