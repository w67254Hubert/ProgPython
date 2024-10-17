# lilista jdnokierunkowa

class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getdata(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data=newdata

    def setNext(self,newnext):
        self.next=newnext

# temp=Node(33)
# print(temp.getdata())
# print(temp.getNext())


class unOrderdList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None

    def add(self,item):
        temp= Node(item)
        temp.setNext(self.head)
        self.head=temp

    def size(self):
        current= self.head
        count=0
        while current != None:
            count= count+1
            current = current.getNext()
        return count

    def seartch(self,item):
        current=self.head
        found=False
        while current != None and not found:
            if current.getdata() == item:
                found=True
            else:
                current=current.getNext()
        return found


    def remove(self,item):
        current=self.head
        previous= None
        found=False
        while not found:
                if current.getdata()==item:
                    found=True
                else:
                    previous=current
                    current=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())

#zad2    
    def remItElement(self,i):
        current = self.head
        previous = None
        count = 0

        # pętla szukająca i-tego węzła
        while current is not None and count < i:
            previous = current
            current = current.getNext()
            count += 1
        # Jeśli i-ty węzeł został znaleziony
        if current is not None:
            # Jeśli i-ty węzeł jest głową listy
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    #zad3
    def merge_sorted_lists(list1, list2):
        merged_list = unOrderdList()

        current1 = list1.head
        current2 = list2.head

        # Porównujemy wartości węzłów z obu list i dodajemy je do nowej listy
        while current1 is not None and current2 is not None:
            if current1.getdata() > current2.getdata():
                merged_list.add(current1.getdata())
                current1 = current1.getNext()
            else:
                merged_list.add(current2.getdata())
                current2 = current2.getNext()

        # Dodajemy pozostałe węzły z listy 1, jeśli istnieją
        while current1 is not None:
            merged_list.add(current1.getdata())
            current1 = current1.getNext()

        # Dodajemy pozostałe węzły z listy 2, jeśli istnieją
        while current2 is not None:
            merged_list.add(current2.getdata())
            current2 = current2.getNext()

        return merged_list

    #zad4
    def addsort(self,item):
        temp = Node(item)

        if self.head is None or item <= self.head.getdata():
            
            temp.setNext(self.head)
            # print("to jest pierwszy temp: ", temp.getdata())
            self.head = temp
        else:
            current = self.head
            previous = None

            while current is not None and item > current.getdata():
                previous = current
                # print('to jest previous w while ', previous.getdata())
                current = current.getNext()
                # print('to jest current w while ', current.getdata())

            
            temp.setNext(current)
            # print("to jest temp: ", temp.getdata())
            previous.setNext(temp)
            # print("to jest previous: ", previous.getdata())
        
    
    

#zad 1 i 2 test
# mylist=unOrderdList()
# mylist.add(12)
# mylist.add(1)
# mylist.add(23)
# mylist.add(32)

# print(mylist.size())
# print(mylist.seartch(0))
# print(mylist.seartch(12))
# mylist.remove(1)
# print(mylist.size())

# mylist.remItElement(2)
# print("wielkość",mylist.size())


#zad3 test
# list1 = unOrderdList()
# list1.add(1)
# list1.add(3)
# list1.add(5)

# list2 = unOrderdList()
# list2.add(2)
# list2.add(4)
# list2.add(6)

# merged_list = unOrderdList.merge_sorted_lists(list1, list2)
# print(merged_list.size())
# # Wyświetlenie elementów nowej scalonej listy
# current = merged_list.head

#sprawdzanie czy wyglądu listy po marge
# while current is not None:
#     print(current.getdata())
#     current = current.getNext()

#zad4

list = unOrderdList()
list.addsort(8)
unOrderdList.display(list)
print(".............")
list.addsort(5)
unOrderdList.display(list)
print(".............")
list.addsort(2)
unOrderdList.display(list)
print(".............")
list.addsort(3)
unOrderdList.display(list)
print(".............")

