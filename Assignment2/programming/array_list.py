#Mark Boady
#CS 260
#Linked List Example with Arrays

#Arrays do almost everything we need.
#Most of these are trivial.
#I will reimplement some function to show how they work.
class LinkedList:
    def __init__(self):
        self.data=[]
    #Insert element x at position p in List
    def insert(self,p,x):
        #Put in first position
        if p==0 and len(self.data)==0:
            self.data.append(x)
            return
        #Invalid Position
        if p < 0 or p >= len(self.data):
            return
        #Otherwise Shift all elements
        if p == len(self.data):
            self.data.append(x)
            return
        next_val = self.data[p]
        self.data[p]=x
        position=p+1
        while(position < len(self.data)):
            temp = self.data[position]
            self.data[position]=next_val
            next_val=temp
            position+=1
        #the loop ends when we reach end of array
        self.data.append(next_val)
    #Locate
    def locate(self,x):
        i=0
        while i < len(self.data):
            if(self.data[i]==x):
                return i
            i+=1
        #Not Found
        return -1
    #Retrieve
    def retrieve(self,p):
        if p < 0 or p >= len(self.data):
            return None
        else:
            return self.data[p]
    #Remove an Element, shift everything down
    def delete(self,p):
        if(p<0 or p >= len(self.data)):
            return
        #Move to last element
        while(p+1 <= len(self.data)-1):
            self.data[p]=self.data[p+1]
            p+=1
        self.data.pop()
    #Next and Previous just give index info
    def next(self,p):
        return p+1
    def previous(self,p):
        return p-1
    def MakeNull(self):
        self.data=[]
    #First Element
    def first(self):
        return 0
    #Print
    def __str__(self):
        result="[ "
        for x in self.data:
            result+=str(x)+" "
        result+="]"
        return result
    #Last Element
    def last(self):
        if(len(self.data)==0):
            return 0
        return len(self.data)-1

#Testing
if __name__=="__main__":
    import random
    L = LinkedList()
    for x in range(100,0,-1):
        L.insert(L.first(),x)
    print("List we are testing:")
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
