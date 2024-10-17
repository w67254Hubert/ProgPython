import random

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.append(item)
    def denqueue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

ppl=['Ala','Ola','Tomek','Olek','Adam']
q=Queue()

for x in ppl:
    q.enqueue(x)

while q.size()>1:
    i=random.randint(1,20)
    while i!=0:
        tym=q.denqueue()
        q.enqueue(tym)
        i=i-1
    q.denqueue()

print(q.items)
