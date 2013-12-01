class Stack():
    def __init__(self):
        self.data = [];
        self.data.append(0);
        
    def pop(self):
        if self.data > 0:
            self.data[0] -= 1;
            return self.data.pop(1);
        else:
            return None;
        
    def push(self, elem):
        if elem :
            self.data.append(elem);
            self.data[0] += 1;
            
    def size(self):
        return self.data[0];
