class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class CLL:
    def __init(self,last=None):
        self.last=last

    def is_empty(self):
        return self.last==None
    
    def insert_at_first(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n        #next will refer to itself
            self.last=n
        else:
            n.next=self.self.last.next
            self.last.next=n

    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n

    def search(self,data):
        if not self.is_empty():
            temp=self.last
            if temp.item==data:
                return temp
            
    def insert_after(self,temp,data):
        pass
        

mylist=CLL()
mylist.insert_at_first(10)