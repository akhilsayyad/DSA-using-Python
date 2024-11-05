from SLL import *
class stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0

    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_first(data)
        self.item_count+=1


    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count-=1

    def peel(self):
        if not self.is_empty():
            print(self.start.item)
        else:
            raise IndexError("Stack underflow")
        
    def size(self):
        print(self.item_count)

s1=stack()
s1.push(10)
s1.push(20)
     