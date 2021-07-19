#Circular queue

class Circular_queue():
    
    def __init__(self,size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        
        
    def enqueue(self,data):
        if self.head==-1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
            
        elif ((self.tail+1)%self.size)==self.head:     #checks if Circular Queue is FUll
            print("Circular Queue Is FUll")
            
        else:
            self.tail = (self.tail+1)%self.size         #since its Circular we use mod size to allocate
            self.queue[self.tail] = data
            
            
    def dequeue(self):
        if self.head==-1:
            print("Queue Is Empty Can't Delete")            #if queue is empty - no element present
        
        
        elif self.head==self.tail:
            self.head = -1
            self.tail = -1
        
        else:
            self.head = (self.head + 1)%self.size                       #otherwise pop first element


    def view(self):
        if self.head==-1:
            print("Queue is Empty, nothing to print")
            
        
        elif self.tail >= self.head:
            print("The circular Queue is : ")
            for i in range(self.head, self.tail+1):
                print(self.queue[i],end=" ")
            print(" ")
        
        else:
            print("The circular Queue Is: ")
            for i in range(self.head,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.tail+1):
                print(self.queue[i],end=" ")
        
        
#driver code
circular = Circular_queue(5)

circular.enqueue(5)
circular.enqueue(6)
circular.enqueue(9)
circular.enqueue(6)
circular.enqueue(2)
circular.view()
circular.dequeue()
circular.dequeue()
circular.enqueue(7)
circular.view()