class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class stack:
    def __init__(self,top=None):
        self.top=top
        self.item_count=0

    def is_empty(self):
        return self.top==None
    
    def push(self,data):
        n=Node(data,self.top)
        self.top=n
        self.item_count+=1
    
    def pop(self):
        if not self.is_empty():
            data=self.top.item
            self.top=self.top.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is Empty")
        
    def peek(self):
        if not self.is_empty():
            print(self.top.item)
        else:
            raise IndexError("Stack is Empty")
        
    def size(self):
        print(self.item_count)

s1=stack()
s1.push(120)
s1.push(320)
s1.push(420)
s1.size()
s1.peek()