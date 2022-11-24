# STEP 1: CREATE A NODE CLASS (characterized by data and next/reference)
from itertools import count


class Node:
  # init method is the equivalent of our constructor
    def __init__(self, data):
      # in javascript (this.data)
        self.data = data
      # None:key word for empty value
      # in javascript (this.next)
        self.next = None

# -----------------------------------------------------------------------------------------------------------------

# print(first_node) # Result gives us reference of newly created obj (<__main__.Node object at 0x000001EEE89CED70>)

# STEP 2: CREATE A LINKED LIST (chain of nodes)
class LinkedList:
  def __init__(self):
    # initailized by the head
    self.head = None
    number = 0

    # We also define the size here

  # we will traverse through our linked list
  # conditions to check:
  #   1. Is our linked list empty (Print a message)
  #   2. Is our linked list NOT empty (Print the data in each node)

  # Traversal operation
  def print_LinkedList(self):
    if self.head is None:
      print("Linked list is null!")
    else:
      # introduce our nd variable (represents the head of node). We can use this to navigate to next node in our list
      nd = self.head
      while nd is not None:
        print(nd.data,"--->",end=" ")
        nd = nd.next

  # when inserting an element to the list, we need to mention the data to be entered to the list
  def add_at_beginning(self, data):
    # Creating a node from the Node class with the data ([data, none])
    new_node = Node(data)
    # We need to change reference of the new node with the link of the previous first node of the linked list
    new_node.next = self.head
    # Store the reference of new node in the self.head
    self.head = new_node
    number+=1

  def add_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      nd = self.head
      while nd.next is not None:
        nd = nd.next
      nd.next = new_node
    
    

list1 = LinkedList()
list1.add_at_beginning(10)
list1.add_at_beginning(15)
list1.add_at_end(30)
list1.print_LinkedList()
