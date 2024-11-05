class deque:
    def __init__(self):
        self.items=[]
        self.item_count=0
    
    def is_empty(self):
        return len(self.items)==0
    
    def insert_front(self,data):
        return self.items.insert(0,data)
    
    def insert_rear(self,data):
        return self.items.append(data)
    
    def delete_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Deque is Empty")
    
    def delete_rear(self):
        if not self.is_empty():
            return self.items.pop(-1)
        else:
            raise IndexError("Deque is Empty")
        
    def get_front(self):
        print(self.items[0])

    def get_rear(self):
        print(self.items[-1])

    def size(self):
        print(len(self.items))

dq=deque()
dq.insert_front(10)
dq.insert_rear(20)

dq.insert_front(5)
dq.insert_rear(30)
dq.delete_front()
dq.delete_rear()
dq.get_front()
dq.get_rear()
dq.size()