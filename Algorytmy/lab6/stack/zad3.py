
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return  self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

str='}])([{'
s= Stack()
l=len(str)
naw = [['(',')'],['[',']'],['{','}']]

print(naw)

for x in naw:
    i=0
    b=0
    s.__init__()
    
    while i<l:

        if str[i]==x[0]:
            s.push(str[i])
        else:
            if s.isEmpty() and str[i]==x[1]:
                # print("zamykajacy w ineksie",i)
                b=b+1
            elif str[i]==x[1]:
                s.pop()
            else:
                pass
        i+=1

    if s.size()>0 and b>0:
        print("złe ustawienie 'końcowych' nawiasów: ",x[1],x[0])
        
    if b==0 and s.isEmpty(): 
            print("wszystko dobrze ",x[0],x[1])

    if s.size()>0:
        print("za durzo otwierających ",x[0]," ", s.size())
    if b>0:
        print("za durzo zamykajacych ",x[1]," ", b)

    print()