class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None

	
	#Inserting at the begining of a linkedlist
	def push(self, new_data):
		new_node = Node(new_data)

		new_node.next = self.head
		self.head = new_node

	
	#Inserting after a node in linked list
	def insert_after(self, new_data, prev_node):
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node


	#Insert at the end of linkedlist
	def append(self,new_data):
		new_node = Node(new_data)

		temp_node = self.head
		while temp_node.next:
			temp_node = temp_node.next
		temp_node.next = new_node

	#printing the linked list
	def print_list(self):
		temp_node = self.head
		while temp_node:
			print(f'{temp_node.data} -->')
			temp_node = temp_node.next
		
