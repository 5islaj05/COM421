class Node:
  
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

  def link(self, otherNode):
    self.next = otherNode
    otherNode.prev = self

  def __str__(self):
    return self.data.__str__()

class LinkedList:
  
  def __init__(self):
    self.first = None
    self.last = None

  def add(self, data):
    node = Node(data)

    if self.last == None:
      self.first = node
    else:
      self.last.link(node)

    self.last = node

  def get(self, index):
    if index < 0:
      print("Index out of bounds, index must be at least 0")
      return

    currentNode = self.first

    for i in range(0, index, 1):
      if currentNode.next == None:
        print("Index out of bounds, index is greater than list length")
        return

      currentNode = currentNode.next

    return currentNode

#   Main Program

# Create a linked list
list = LinkedList()

# Add some items to it
list.add(4)
list.add(10)
list.add(-7)

# Print the first item
# Expected: 4
print(list.get(0))

# Print the second item
# Expected: 10
print(list.get(1))

# Print the third item
# Expected: -7
print(list.get(2))

# Print the fourth item. Should print an error becaues there
# are not 4 items in the list.
# Expected: Index out of bounds, index is greater than list length
#           None
print(list.get(3))

# Print the item at the -1 index. Should print an error because
# the index cannot be less than 0.
# Expected: Index out of bounds, index must be at least 0
#           None
print(list.get(-1))
