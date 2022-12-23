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
        self.need_X = False
    
    def set_X(self):
        self.operation = ['X']
        self.need_X = True
    
    def resolve_operation(self, first, second):        
        if self.operation[0] == '+':
            self.operation = [first + second]
        elif self.operation[0] == '-':
            self.operation = [first - second]
        elif self.operation[0] == '*':
            self.operation = [first * second]
        elif self.operation[0] == '/':
            self.operation = [first / second]
    
    def resolve_reverse_operation(self, first, second, need_result):
        if self.operation[0] == '+':
            result = need_result-first if first!=None else need_result-second
        elif self.operation[0] == '-':
            result = first-need_result if first!=None else need_result+second
        elif self.operation[0] == '*':
            result = need_result/first if first!=None else need_result/second
        elif self.operation[0] == '/':
            result = first/need_result if first!=None else need_result*second
        self.operation = [need_result]
        return result
        
    
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
        if self.operation[0] == 'X':
            return None
        return self.operation[0]
    
    def __str__(self):
        string = self.name + " "
        string += "X : " if self.need_X else "O : "
        for el in self.operation:
            string += str(el) + " "     
        return string
        
        
class Monkey_Manager:
    def __init__(self, day_input):
        self.monkeys = {}
        for monkey_info in day_input:
            monkey = Monkey(monkey_info)
            self.monkeys[monkey.name] = monkey
    
    def get_X(self, name):
        first, second = self.monkeys[name].operation[1:]
        value_1 = self.get_result(first)
        value_2 = self.get_result(second)
        if value_1 == None:
            return self.get_reverse_result(first, value_2)
        return self.get_reverse_result(second, value_1)
        
    def get_reverse_result(self, name, need_value):
        c_monkey = self.monkeys[name] 

        while c_monkey.operation != ['X']:
            first, second = c_monkey.operation[1:]
            first = self.monkeys[first]
            second = self.monkeys[second]
    
            need_value = c_monkey.resolve_reverse_operation(first.result(), second.result(), need_value)        
            if first.need_X:
                c_monkey = first
            else:
                c_monkey = second
                
        return need_value
    
    def get_result(self, name):
        operations = [self.monkeys[name]]
        while operations:           
            c_monkey = operations[-1]
            first, second = c_monkey.operation[1:]
            first = self.monkeys[first]
            if first.result() == None and not first.need_X:
                operations.append(first)
                continue
            second = self.monkeys[second]
            if second.result() == None and not second.need_X:
                operations.append(second)
                continue
            if first.need_X or second.need_X:
                c_monkey.need_X = True
                operations.pop()
                continue
            c_monkey.set_numbers([first, second])
            operations.pop()
        return self.monkeys[name].result()
    
    def __str__(self):
        string = ""
        for m in self.monkeys.values():
            string += str(m) + "\n"
        return string[:-2]

if __name__ == "__main__":
    day_input = read_file("input.txt")
    
    manager = Monkey_Manager(day_input)

    manager.monkeys['humn'].set_X()

    
    result = manager.get_X('root')
    print("----")
    #print(manager)
    print("----")
    print(result)
    

        
        
        
         
    
    
