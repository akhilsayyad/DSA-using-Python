class stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        if len(self.items)==0:
            print("Empty stack")
    
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
            raise IndexError("Stack is empty")
        

    def size(self):
        print(len(self.items))
    

s1=stack()
# s1.is_empty()
s1.push(10)
s1.push(210)
s1.push(130)
s1.pop()
s1.size()
s1.peek()
