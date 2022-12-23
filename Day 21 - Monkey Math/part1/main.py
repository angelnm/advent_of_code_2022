def read_file(namefile):
    with open(namefile, 'r') as f:
        lines = f.read().splitlines()
    return lines

class Monkey:
    def __init__(self, monkey_info):
        name, operation = monkey_info.split(':')
        operation = operation.split()
        if len(operation)==1:
            operation[0] = float(operation[0])
        else:
            tmp = operation[0]
            operation[0] = operation[1]
            operation[1] = tmp
            
        self.name = name
        self.operation = operation
    
    def resolve_operation(self, first, second):        
        if self.operation[0] == '+':
            self.operation = [first + second]
        elif self.operation[0] == '-':
            self.operation = [first - second]
        elif self.operation[0] == '*':
            self.operation = [first * second]
        elif self.operation[0] == '/':
            self.operation = [first / second]
    
    def need_name(self):
        if len(self.operation)==1:
            return None
        return self.operation[1:]

    def set_numbers(self, monkeys):
        for n in monkeys:
            self._set_number(n)

    def _set_number(self, monkey):
        if len(self.operation) == 1:
            return
        for idx, n in enumerate(self.operation[1:]):
            if n == monkey.name:
                self.operation[idx+1] = monkey.result()
         
    def result(self):
        if len(self.operation)>1:
            first = self.operation[1]
            second = self.operation[2]
            if isinstance(first, float) and isinstance(second, float):
                self.resolve_operation(first, second)
                return self.operation[0]
            return None
        return self.operation[0]
    
    def __str__(self):
        string = self.name + ": "
        for el in self.operation:
            string += str(el) + " "     
        return string
        
        
class Monkey_Manager:
    def __init__(self, day_input):
        self.monkeys = {}
        for monkey_info in day_input:
            monkey = Monkey(monkey_info)
            self.monkeys[monkey.name] = monkey
       
    def get_result(self, name):
        operations = [self.monkeys[name]]
        n_process = 0
        while n_process >= 0:              
            monkey = operations[n_process]
            if monkey.result() == None:
                next_monkeys = monkey.need_name()
                for nm in reversed(next_monkeys):
                    operations.insert(n_process+1, self.monkeys[nm])
                n_process += 1
                continue
            
            previous = operations[n_process-1]
            if previous.result() == None:
                n_process += 1
                continue
            n_process -= 2
            if n_process<0:
                return monkey.result()
            operations[n_process].set_numbers([monkey, previous])
            del operations[n_process+1:n_process+3]


  
if __name__ == "__main__":
    day_input = read_file("input.txt")
    
    manager = Monkey_Manager(day_input)  
    result = manager.get_result('root')
    print(result)
    

        
        
        
         
    
    
