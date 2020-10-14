#cretes a class called Stack
class Stack:
  #__init__ is used to create the array (stack)
  def __init__(self): 
    self.internalArray = []

    #the __str__ function makes sure the stack when being printed shows the array
  def __str__(self): 
    return self.internalArray.__str__()

  #This is the push method which adds an item to the stack
  def push(self, item):
    self.internalArray.append(item)
   
  #pop method which removes  basically removes an item from the stack
  def pop(self):
    if (len(self.internalArray) == 0): #test to see if stack is empty so no further processing occurs, same with errors
      print("You cannot pop an empty stack!")
      return #ends function by returning nothing (as the print above does everything needed)
    else:
      removed = self.internalArray[-1] #stores the removed value so it can be used for other purposes such as showing what was removed
      del self.internalArray[-1] #removes the item from the stack (array)
      return removed #lets the code know the variable returned was the result of the function

  #Function peek is used to show the newest item added to the stack without popping it. uses the same way in pop to show value.
  def peek(self):
    
    return  self.internalArray[-1]

print("Stack program example")
stack1 = Stack() #creates the stack program in a variable which can be used as a shotcut
print("Demonstrating push")
 #adds letter A, B and C to the stack
stack1.push("A")
stack1.push("B")
stack1.push("C")
print(stack1) #prints out the stack to show results

print("Demonstrating peek and pop")
#Pops the Letter B and C then adds the letter D and
stack1.pop()
stack1.pop()
stack1.push("D")
print("Peek:",stack1.peek()) #improvment to the code could be where we dont use print and just call the function 
print(stack1)
# The end