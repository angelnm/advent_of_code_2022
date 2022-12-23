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

def get_max_reward(reward, path):
    valve_data = []
    
    for valve in reward:
        if valve not in path:
            valve_data.append([valve] + reward[valve])
    
    valve_data = sorted(valve_data, key=lambda x: x[1], reverse=True)   
    return valve_data

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
    def __init__(self, _time, _pressure, _path=[]):
        self.time = _time
        self.pressure = _pressure
        self.path = _path
        
    def get_score(self):
        ratio = self.pressure/(self.time)
        return self.pressure + ratio*self.time
        
    def __str__(self):
        string = str(self.pressure) + " " + str(30-self.time) + " " + str(self.path)
        return string

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
    
    beam_size = 1000
    
    path_info = []
    #path_info.append(Path_Information(30-9, 1326, ['DD', 'BB', 'JJ']))
    path_info.append(Path_Information(30, 0))
    
    i = 0
    while len(path_info[0].path)<len(valves):
        new_path_info = []
        for info in path_info:
            start = 'AA' if not info.path else info.path[-1]
            
            rewards = get_graph_rewards(valves, valves[start], info.time)
            valve_data = get_max_reward(rewards, info.path)[:beam_size]
            
            new_path_info.append(Path_Information(info.time, info.pressure, info.path+[start]))
            for data in valve_data:
                if data[1] != 0:
                    new_path_info.append(Path_Information(data[2], info.pressure + data[1], info.path+[data[0]]))
        
        path_info = sorted(new_path_info, key=lambda x: x.get_score(), reverse=True)[:beam_size]

        
    for info in path_info[:2]:
        print(info.pressure, info.time)
        print(info.path)
         
    
    
