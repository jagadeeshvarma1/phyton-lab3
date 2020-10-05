class Node: #creating a class Node
    def __init__(self,data): #self executing constructor
        self.data=data
        self.next=None
#creating a class linked list with required functions        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        if self.tail is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next
    def add_at_beginning(self,data): #method for adding an ele at beginning
        temp=Node(data)
        temp.next=self.head
        self.head=temp        
    def disp(self):
        cur=self.head 
        while cur is not None:
            print(cur.data,end=" ")
            cur=cur.next
#program execution starts here            
l=LinkedList()
n=int(input("size:"))
print("elements:")
for i in range(n):
    data=int(input())
    l.append(data)
k=int(input("element to add at beginning"))    
l.add_at_beginning(k) #calling add at beginning method to add element  
l.disp()            
