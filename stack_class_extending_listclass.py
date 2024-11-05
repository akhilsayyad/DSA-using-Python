class list:
    def __init__(self):
        self.items=[]

class stack(list):
    def __init__(self):
        super().__init__()

    def is_empty(self):
        if len(self.items)==0:
            print("Emtpy stack")

    def push(self,data):
        return self.items.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")
        
    def peek(self):
        if not self.is_empty():
            print(self.items[-1])
        else:
            raise IndexError("Stack is Empty")
    
    def size(self):
        print(len(self.items))

    # def insert(self,item,index):
    #     if 

s2=stack()
s2.push(10)
s2.push(210)
s2.push(310)
s2.pop()
s2.peek()

s2.size()

