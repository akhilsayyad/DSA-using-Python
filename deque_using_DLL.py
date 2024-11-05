class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class Dqueue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.rear==None
    
    def insert_front(self,data):
        n=Node(data,self.front)
        if self.is_empty():
            self.front=n
            self.rear=n

        else:
            n.next=self.front
            self.front.prev=n
            self.front=n
        self.item_count+=1

    def insert_rear(self,data):
        n=Node(self.rear,data)
        if self.is_empty():
            self.front=n
            self.rear=n
        else:
            self.rear.next=n
            n.prev=self.rear
            self.rear=n
        self.item_count+=1
        
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count-=1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.item_count-=1

    def get_front(self):
        print("Front element is::",self.front.item)

    def get_rear(self):
        print("Rear element is::",self.rear.item)
    
    def size(self):
        print(f"There are {self.item_count} elements in Dequeue")

dq2=Dqueue()
dq2.insert_front(11)
dq2.insert_front(12)

dq2.insert_rear(3)

dq2.delete_front()
# dq2.get_front()

# dq2.get_front()
dq2.delete_rear()
dq2.size()
dq2.get_rear()


    