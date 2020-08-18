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


	#deleting a node from key
	def delete_node_from_key(self, key):
		temp = self.head
		prev = None
		
		if temp is not None:
			if self.head.data == key:
				self.head = self.head.next
				temp = None
				print(f'Key {key} deleted..!')
				return

		while temp:
			print("data", temp.data)
			if temp.data == key:
				break
			
			prev = temp
			temp = temp.next
		
		if temp is None:
			print("Key not exists in the the linkedlist")	
		else:
			prev.next = temp.next
			temp = None	
			print(f'Key {key} deleted..!')


	#deleting a node by index
	def delete_node_from_index(self, index):
		if self.head is None:
			print("Can't delete, Linkedlist is empty")
			return
		
		temp = self.head
		prev = None
		count = 0
		
		if index == 0:
			self.head = temp.next
			temp = None
			print("Deleted node at index 0")
			return
		
		print('temp', temp)
		while count < index and temp is not None:
			prev = temp
			temp = temp.next
			count += 1
					
		print("count", count)
		if count < index:
			print(f'No node at position {index}')
		else:
			prev.next = temp.next
			temp = None
			print(f'Node deleted at index {index}')


	#Delete a linkedlist
	def delete_ll(self):
		if self.head is None:
			print("Linkedlist is already empty")
			return

		current = self.head
		while current:
			print(f'Deleting value {current.data}')
			prev = current
			current = current.next
			del prev.data
			del prev.next
	
		self.head = None

		print("All the elements from the linkedlist are deleted")


	#Length of a linkedlist by iterative way
	def list_length_iterative(self):
		temp = self.head
		count = 0
		while(temp):
			temp = temp.next
			count += 1

		print("Length of the linkedlist is:", count)


	##Length of a linkedlist by recursive method
	def list_length_reccursive(self, start):
		if start is None:
			return 0
		return 1+ self.list_length_reccursive(start.next)


	def print_list_length(self):
		print("Length of the list is", self.list_length_reccursive(self.head))



	#Search in a linkedlist iteratively
	def search_list_iterative(self, key):
		temp = self.head
		while temp:
			if temp.data == key:
				return True
			temp = temp.next

		return False


	#Search in a linkedlist recursively
	def search_list_recursive(self, node, key):
		if node is None:
			return False

		if node.data == key:
			return True

		return self.search_list_recursive(node.next, key)


	def print_search_list_recursive(self,key):
		print(self.search_list_recursive(self.head, key))
	

	#Get nth node of a linkedlist
	def get_nth_node_iterative(self, N):	
		current = self.head
		count = 0
		while current:
			if count == N:
				print("Nth node data is :", current.data)
				return
			current = current.next
			count += 1

		print("Nth node not available")
		
