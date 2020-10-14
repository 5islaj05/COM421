class Stack:
  def __init__(self):
    self.internalArray = []
    print("")
  def push(self, item):
    self.internalArray.append(item)
   

  def pop(self):
    self.internalArray.remove(item)

  def __str__(self):
    return self.internalArray.__str__()
    print(self)



print ("\n \n \n")
print("other test")
a = []
a.append(111)
a.append(222)
a.append(333)
print(a)

