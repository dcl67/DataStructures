#Mark Boady
#CS 260
#Linked List Example with Pointers

class Node:
    def __init__(self,v,n=None):
        self.value = v
        self.next = n
    def __str__(self):
        result = "["+str(self.value)+"]->"
        return result
    def getValue(self):
        return self.value
    def setValue(self,v):
        self.value = v
    def getNext(self):
        return self.next
    def setNext(self,n):
        self.next = n


#A linked List
#A linked list is just a bunch of nodes

class LinkedList:
    def __init__(self):
        self.start= None
    #Insert element x at position p into List
    def insert(self,p,x):
        if p==None and self.start==None:
            #insert at front
            self.start = Node(x)
            return
        #P is the node at position
        old_val = p.getValue()
        p.setValue(x)
        new_node = Node(old_val,p.getNext())
        p.setNext(new_node)
    #Locate element x in List
    def locate(self,x):
        current = self.start
        while current != None:
            if current.getValue()==x:
                return current
            current = current.getNext()
        return False
    #Retrieve element at position p
    def retrieve(self,p):
        if p==None:
            return None
        else:
            return p.getValue()
    #Delete element at position p
    def delete(self,p):
        if p==None:
            return
        #First Element
        if p==self.start:
            self.start=p.getNext()
            return
        #In the middle somewhere!
        before = L.previous(p)
        before.setNext(p.getNext())
    #Return next and previous positions
    def next(self,p):
        if p==None:
            return None
        else:
            return p.getNext()
    def previous(self,p):
        if p==None:
            return None
        #Look for it!
        if self.start==p:
            return None
        current = self.start
        while current != None:
            if current.getNext()==p:
                return current
            current = current.getNext()
        return None#Didn't Find
    #Make an empty list
    def MakeNull(self):
        self.start=None
    #Find first position in list
    def first(self):
        return self.start
    #Print the list
    def __str__(self):
        current = self.start
        result=""
        while current != None:
            result=result+str(current)
            current = current.getNext()
        result=result+"None"
        return result
    #Last
    def last(self):
        current = self.start
        if current==None:
            return None
        while current.getNext()!=None:
            current=current.getNext()
        return current

if __name__=="__main__":
    import random
    L = LinkedList()
    for x in range(100,0,-1):
        L.insert(L.first(),x)
    print("List we Created: ")
    print(L)
    print("Where is eleven:")
    print(L.locate(11))
    print("What is the first element?")
    print(L.retrieve(L.first()))
    p = L.locate(28)
    print("What is after 28?")
    print(L.retrieve(L.next(p)))
    print("What is before 28?")
    print(L.retrieve(L.previous(p)))
    print("What does it look like without 28?")
    L.delete(p)
    print(str(L))
    print("Can we delete the first element?")
    L.delete(L.first())
    print(str(L))
    print("What is the last item?")
    print(L.retrieve(L.last()))

