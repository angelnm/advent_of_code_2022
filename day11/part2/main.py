class Monkey:
    def __init__(self, _id, _items, _ope, _test, _true, _false):
        self.id = _id
        self.items = _items
        self.ope = _ope
        self.test = _test
        self.true = _true
        self.false = _false
        
        self.n_inspect = 0
        
    def inspect(self):
        for i in reversed(range(len(self.items))):
            self.n_inspect += 1
            
            worry_level = self.items.pop(i)
            worry_level = self.perform_operation(worry_level)
            
            if worry_level > mcm:
                worry_level = worry_level%mcm
            
            if worry_level%self.test == 0:
                self.throw_item(self.true, worry_level)
            else:
                self.throw_item(self.false, worry_level)
    
    def perform_operation(self, level):
        a = self.ope[0] if self.ope[0]!='old' else level
        b = self.ope[2] if self.ope[2]!='old' else level
        
        if self.ope[1] == '+':
            return a+b
        elif self.ope[1] == '-':
            return a-b
        elif self.ope[1] == '/':
           return a/b
        elif self.ope[1] == '*':
           return a*b
    
    def get_inspections(self):
        return self.n_inspect
    
    def update_items(self):
        self.items = self.new_items
    
    def throw_item(self, monkey, item):
        monkies[monkey].items.append(item)
        
    def __str__(self):
        return str(self.n_inspect) + ' ' + str(self.items)

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

monkies = []
mcm = 1
for i in range(0, len(lines), 7):
    c_id = int(lines[i].split()[1][:-1])
    
    c_items = lines[i+1].split()[2:]
    c_items[:-1] = [x[:-1] for x in c_items[:-1]]
    c_items = [int(x) for x in c_items]
    
    c_ope = lines[i+2].split()[3:]
    c_ope = [int(x) if '0'<=x[0]<='9' else x for x in c_ope]
    
    c_test = lines[i+3].split()[3]
    c_test = int(c_test)
    
    c_true = lines[i+4].split()[5]  
    c_true = int(c_true)
    
    c_false = lines[i+5].split()[5]
    c_false = int(c_false)
    
    mcm *= c_test
    monkies.append(Monkey(c_id, c_items, c_ope, c_test, c_true, c_false))

for round in range(10000):
    for monkey in monkies:
        monkey.inspect()

inspections = [x.get_inspections() for x in monkies]
inspections.sort()
print(inspections[-1]*inspections[-2])


