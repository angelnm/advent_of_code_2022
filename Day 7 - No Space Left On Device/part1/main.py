with open('input.txt', 'r') as f:
    lines = f.read().splitlines()    

class Folder:
    def __init__(self, name, before=None, size=0, file=False):
        self.name = name
        self.size = size
        self.before = before
        self.after = []
        self.file = file
        
    
    def get_father(self):
        return self.before
    
    def get_name(self):
        return self.name
    
    def add_size(self, size):
        self.size += size
        if self.before:
            self.before.add_size(size)
    
    def add_file(self, name, size=0):
        new_child = Folder(name, self, size, True)
        self.add_size(size)
        self.after.append(new_child)
    
    def get_child(self, name):
        for child in self.after:
            if name == child.get_name():
                return child
        new_child = Folder(name, self)
        self.after.append(new_child)
        return new_child
    
    def get_sum(self):
        total_sum = 0
        if not self.file and self.size!=0 and self.size<100000:
            total_sum += self.size
        for i in self.after:
            total_sum += i.get_sum()
        return total_sum
    
    def __str__(self, tab=0):
        string = ''
        for i in range(tab):
            string += ' '
        string += '-'+self.name
        if self.size!=0:
            string+=' '+str(self.size)
        string+='\n'
        
        for i in self.after:
            string+=i.__str__(tab+1)
        
        return string

computer = None
current = computer
for line in lines:
    data = line.split()
    if data[0]=='$':
        if data[1]=='cd':
            if data[2]=='..':
                current = current.get_father()
            elif data[2]=='/':
                if computer==None:
                    computer=Folder('/')
                current=computer
            else:
                current = current.get_child(data[2])
        elif data[1]=='ls':
            pass
    else:
        if '0'<=data[0][0]<='9':
            current.add_file(data[1], int(data[0]))
                       
print(computer)
print(computer.get_sum())