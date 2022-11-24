#  impelement a linked list in a language of your preference
# 1. Print
# 2. Insert at the beginning
# 3. Insert at the end
class Node:
  # init method is the equivalent of our constructor
    def __init__(self, data):
        self.data = data
      # None:key word for empty value
        self.next = None
# Creating a node
first_node = Node(12)

print(first_node)