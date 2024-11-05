class priorityqueue:
    def __init__(self):
        self.items=[]
        self.item_count=0

    def is_empty(self):
        return len(self.items)==0
    
    def push(self,data,priority):
        return self.items.insert(priority,data)
        self.item_count+=1
    
    def pop(self,data):
        return self.items.remove(data)
        self.item_count-=1

    def size(self):
        print(self.item_count)

    def printlist(self):
        print(self.items)

pq=priorityqueue()
pq.push("Akhil",1)
pq.push("Sayyad",2)
pq.push("Nijam",1)
pq.push("Thinker",3)
pq.push("Sayyad",2)
pq.push("Pqr",2)
pq.pop("Sayyad")
pq.printlist()