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
  
  #printing the linked list
  def print_list(self):
    temp = self.head
    while temp:
      print(f'{temp.data} -->')
      temp = temp.next

  #Find the middle element in a linked list
  def find_middle_element_traversing(self):
    if self.head is None:
      print("Linked list is empty")
      return

    temp = self.head
    count = 0
    while temp:
      temp = temp.next
      count += 1

    temp = self.head
    for _ in range(count//2):
      temp = temp.next

    print(f'The middle element of the linked list is {temp.data}')

  #Find middle element of a linkedlist by using 2 pointers
  def find_middle_element_two_pointer(self):
    if self.head is None:
      print("Linked list is empty")
      return

    if self.head.next is None:
      print("Middle element is :", self.head.data)
      return

    fast_ptr = self.head
    slow_ptr = self.head

    while fast_ptr and fast_ptr.next:
      fast_ptr = fast_ptr.next.next
      slow_ptr = slow_ptr.next

    print("Middle element is :", slow_ptr.data)

