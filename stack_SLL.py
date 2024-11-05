from SLL import *
class stack:
    def __init__(self):
        self.my_list=SLL()
        self.item_count=0

    def is_empty(self):
        return self.my_list.is_empty()
    
    def push(self,data):
        self.my_list.insert_at_first(data)
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            self.my_list.delete_first()
            self.item_count-=1
    
    def peek(self):
        if not self.is_empty():
            print(self.my_list.start.item)
        
    def size(self):
        print(self.item_count)


s=stack()
s.push(10)
s.push(20)
s.push(30)
# s.peek()
s.size()