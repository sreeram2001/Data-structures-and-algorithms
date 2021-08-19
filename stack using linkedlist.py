
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class Stack:
    def __init__(self):
        self.head = None
        
        
    #Is-empty
    def isempty(self):
        
        if self.head == None:
            print("Stack Is Empty")
            
        else:
            print("Stack is not Empty")
            
        

    #push-element
    def push(self,data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            
        else:
            temp = self.head
            
            while temp.next != None:
                temp = temp.next
                
            temp.next = node
                
                
                
    #pop-element 
    def pop(self):
        
        if self.head is None:
            print("Stack Empty")
            
        else:
            temp = self.head
            
            while temp.next.next is not None:
                temp = temp.next
                
            pop = temp.next
            temp.next = None
            print("Popped out Element :",pop.data)
            
            
            
    
    #top-element      
    def top(self):
        
        if self.head is None:
            print("Empty Stack")
            
        else:
            temp = self.head
            
            while temp.next is not None:
                temp = temp.next
                
            print("Top Element :",temp.data)
            

            
    #traversal       
    def traversal(self):
        
        if self.head is None:
            print("Stack Is Empty")
            
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
                
            
            
            
#DRIVER CODE
stack = Stack()
stack.push(45)
stack.push(67)
stack.push(99)

stack.isempty()
stack.top()
stack.pop()

stack.traversal()
            
            

