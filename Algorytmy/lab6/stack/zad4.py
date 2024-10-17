
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





str= '7 3 + 5 2 - 2 ^ * ='
lisStr=str.split(' ')
print(lisStr)
s= Stack()
l=len(lisStr)
i=0
b=0

print("tak wygląda dzialanie ", str)

for i in range(l):
    if '+'==lisStr[i]:
        x=s.pop()
        y=s.pop()
        s.push(y+x)
        
    elif '-'==lisStr[i]:
        x=s.pop()
        y=s.pop()
        s.push(y-x)
    elif '*'==lisStr[i]:
        x=s.pop()
        y=s.pop()
        s.push(y*x)

    elif '/'==lisStr[i]:
        x=s.pop()
        y=s.pop()
        s.push(y/x)

    elif '^'==lisStr[i]:
        x=s.pop()
        y=s.pop()
        s.push(y**x)
    elif '='==lisStr[i]:
        print("wynik", s.peek())

    else:
        s.push(int(lisStr[i]))




# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# s.push('34')
# print(s.isEmpty())
# print(s.size())
# s.pop()
# print(s.size())
# print(s.peek())