#Search for an element in a doubly linked list
#node class
class node:
	#constructor
	def _init_(self,data):
		#instances
		self.data = data
		self.prev = None
		self.next = None
#linkedlist class
class DLinkedList:
	def _init_(self):
		#initialization
		self.head = None
#printing list
	def display(self):
		ele = []
		cur = self.head
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print("Doubly LinkedList: ",ele)
#counting no of elements in the linked list
	def searchNodes(self,data):
		cur = self.head
		while cur:
			if cur.data == data:
				return True
			cur = cur.next
		else:
			return False

#initialization
d = DLinkedList()
#creating nodes and adding it to the lnked list
d.head = node(10) # head ==> 10
d.head.next = node(20) # 10 --> 20
d.head.next.next = node(30) # 10 --> 20 --> 30
d.head.next.next.next = node(40) # 10 --> 20 --> 30 --> 40
#function calling
d.display()
x = int(input("Enter search element: "))
print(d.searchNodes(x))
