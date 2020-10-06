#Search for a item in a linked list   
class node:
	def _init_(self,data):
		self.data = data
		self.next = None
#linkedlist Class
class LinkedList:
	def _init_(self):
		#initialization
		self.head = None
		self.tail = None

	#adding elements
	def append(self,data):
		new_node = node(data)
		#if empty
		if self.head == None and self.tail == None:
			self.head = new_node
			self.tail = new_node
		#if not empty
		else:
			self.tail.next = new_node
			self.tail = new_node

	#printing elements
	def display(self):
		ele = []
		cur = self.head 
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print("Linked List: ",ele)

	#inserting the node at places other than the start or end node
	def AtMid(self,pre_node,data):
		new_node = node(data)
		temp = self.head 
		while temp:
			if temp.data == pre_node: 
				break
			temp = temp.next
		n = temp.next
		temp.next = new_node
		new_node.next = n



l= LinkedList()
n = int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(n):
	k = int(input())
	l.append(k)

print("Before: ")
l.display()


x = int(input("Enter previous node: "))
y = int(input("Enter element to be placed: "))
l.AtMid(x,y)
print("New: ")
l.display()
