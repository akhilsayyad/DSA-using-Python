class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    
    def is_empty(self):
        return self.rear==None
    
    def enqueue(self,data):
        N=Node(data)
        if not self.is_empty():
            self.rear.next=N
            self.rear=N
        else:
            self.front=N
            self.rear=N
        self.item_count+=1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")

        elif self.front==self.rear:
            self.front==None
            self.rear==None

        else:
            self.front=self.front.next
        self.item_count-=1

    def get_front(self):
        print(self.front.item)

    def get_rear(self):
        print(self.rear.item)

    def size(self):
        print(self.item_count)


q1=queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
# q1.size()
q1.dequeue()
q1.get_front()
q1.get_rear()
print(q1.is_empty())