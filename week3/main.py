class Queue:
  def __init__(self, capacity):
    self.front = 0 #value used when you remove value
    self.back = 0 #value used when you add item to list
    self.capacity = capacity #how big the queue is
    self.internalArray = [None] * capacity #creates array

  def add(self, item): #the adding function

   self.internalArray[self.back] = item #adds the item (defined by user) into the queue


   self.back += 1  #makes sure the program moves into the next bit of the queue, ready to add the item

   #Makes the program when doing the next add start at the front of the queue 
   if (self.back >= self.capacity):
     self.back = 0

    


  #removes an item from the queue
  def remove(self): 
  #Upon being called it'll remove the first item in the queue then the next in the queue till it reaches the end of the array which then resets to the front of the queue

    # sets the value to the queue 
    item = self.internalArray[self.front]  

    #removes the value from the queue 
    self.internalArray[self.front] = None 
    
    #makes sure the next time it removes an item from the queue it removes the next item in the queue
    self.front += 1

    if self.front >= self.capacity:
      #makes sure  the next remove  isnt trying to remove an item that doesnt exist in the queue thus returning but returns to the front of the queue
      self.front = 0 
      

      return item #returns

  def size(self):  #finds how many items are left in the queue to be processed
    count = 0 #reset counter if been used before
    for i in range(0, self.capacity, 1): #loops through the queue
      if self.internalArray[i] != None: #checks if the value in the queue is not None and adds 1 to the count variable if there is one
        count += 1
    return count #returns how many times it found a value that isnt "None"


  def __str__(self):
   # makes it where the queue is printed not the memory address of the array (queue)
    return self.internalArray.__str__()


myQueue = Queue(5) #Creates the queue with the capacity of 5 (an array of 5 containing nothing)
print(myQueue) # displays the empty queue

#adds  items to the queue 
myQueue.add("apple") 
myQueue.add("banana")
myQueue.add("pear")

print() 
print("Queue:",myQueue) #displays the stuff in queue
myQueue.remove() #removes an item from the array 
print("Queue:",myQueue) #displays stuff in the queue
print() #adds space to make it easier to view size
print("Queue size:",myQueue.size())