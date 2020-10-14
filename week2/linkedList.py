class Node: #creates the class called Node to contain the functions
  
  #init function used to setup the 3 attributes which is needed to store the "data" of the node and the link to the Next and Previous node
  def __init__(self, data):
    self.data = data #data is going to be what the user sets
    #we dont need anything as this has just be set up
    self.prev = None 
    self.next = None

  #important function to make sure  the nodes  are linked
  def link(self, otherNode):
    self.next = otherNode #next link
    otherNode.prev = self 
    #previous link

  #Used to return data in a readable way
  def __str__(self):
    return self.data.__str__()

#Creating the actual linked list
class LinkedList:
  
  #init process used to create two variables used to create and add items to list
  def __init__(self):
    self.first = None
    self.last = None

  #Adds to the linked list by using the above Class
  def add(self, data):
    node = Node(data)
    #Checks to see if self.last hasnt got a variable so it can set it to something
    if self.last == None:
      self.first = node
    else:
      self.last.link(node) #links self.last to the node being given by add function (by the user)

    self.last = node #links last to node

  #the function below is used to retrieve a value from the list
  def get(self, index):
    #If the value is lower than 0 then stop code and return error (more efficent)
    if index < 0:
      print("Error: index must be at least 0")
      return

    currentNode = self.first #sets the current Node the code looping through to the first one in the linked list.

    #This will loop till it reaches the end of the linked list
    for i in range(0, index, 1):
      #if the CurrentNode is greater than  of the list then return an error (if you try to look for something not in the index of the linked list this happens)
      if currentNode.next == None:
        print("Error: index is greater than the length of the list")
        return

      currentNode = currentNode.next # Sets the CurrentNode value to what the user is trying to retrieve from the list

    return currentNode #returns the answer the user requested

#creates the nodes
n1 = Node("firstNode")
n2 = Node("secondNode")

#prints out the node value
print("Node 1",n1)
print("Node 2",n2)

n1.link(n2) #links the two nodes together
print(n1.next) #prinks out the next node to n1 
print(n2.prev) #prints out the previous value of n2
print(n1.next) #prints out the previous value of n1
#creates the linked list
list = LinkedList()

#Add a couple items to the linked list
list.add("linked")
list.add("lists")
list.add("are")
list.add("cool")
print() #adds a line break
#Print the 1st item in list
print(list.get(0))
#Print the 2nd item in list
print(list.get(1))
#Print the 3rd item in list
print(list.get(2))
#prints the 4th item in list
print(list.get(3))