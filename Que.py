class queue:
    def __init__(self):
        # self.front=front
        self.rear=[]
        

    def is_empty(self):
        return self.rear==None
    
    def enqueue(self,data):
        return self.rear.append(data)
        

    def dequeue(self):
        if not self.is_empty():
            return self.rear.pop(0)
        else:
            pass

    def get_front(self):
        print(self.rear[0])

    def get_rear(self):
        print(self.rear[-1])

    def size(self):
        print(len(self.rear))

q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.size()

q.get_rear()
q.dequeue()
q.get_front()
