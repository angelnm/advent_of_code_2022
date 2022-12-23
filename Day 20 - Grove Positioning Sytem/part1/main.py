def read_file(namefile):
    with open(namefile, 'r') as f:
        lines = f.read().splitlines()
    return lines


class Node:
    def __init__(self, _number, _before):
        self.number = _number
        self.after = None
        self.before = None
        
        if _before:
            self.set_before(_before)
        
    def set_before(self, _before):
        self.before = _before
        _before.after = self
        
    def __str__(self):
        return str(self.number)
    
class Node_Manager:
    def __init__(self, day_input):
        self.nodes = []
        self.start = None
        
        for number in day_input:
            number = int(number)
            previous_node = None if not self.nodes else self.nodes[-1]
            new_node = Node(number, previous_node)
            
            if number == 0:
                self.start = new_node
            
            self.nodes.append(new_node)
        self.nodes[0].set_before(self.nodes[-1])
    
    def get_position(self, position):
        current = self.start
        for _ in range(position):
            current = current.after
        return current.number
    
    def mix(self):
        for node in self.nodes:
            movement = node.number if node.number>=0 else node.number-1
            
            #print()
            #print(node.number)
            #print(self)
                        
            if movement == 0:
                continue
            
            if node.number>0:
                current = node.after
                movement -= 1
            else:
                current = node.before
                movement += 1
            node.after.set_before(node.before)
            
            for i in range(abs(movement)):
                if movement>0:
                    current = current.after
                else:
                    current = current.before
 
            if current.after == node or current == node:
                continue
            
            current.after.set_before(node)
            node.set_before(current)
            
            #print(self)
    
    def __str__(self):
        
        start = self.nodes[0]
        string = str(start.number) + " "
        current = start.after
        while current!=start:
            string += str(current.number) + " "
            current = current.after          
        return string
  
if __name__ == "__main__":
    day_input = read_file("input.txt")
    
    manager = Node_Manager(day_input)
    #manager.nodes[-1].number = 4
    manager.mix()
    total_sum = 0
    for position in [1000, 2000, 3000]:
        number = manager.get_position(position)
        total_sum += number
    print(total_sum)
    #print(manager)
    

        
        
        
         
    
    
