
#linkedlist

#For - Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
        
    def __init__(self):
        self.head = None


        
    #traveral - print
    def traversal(self):
        
        if self.head is None:
            print("Linkedlist is Empty")
            
        else:
            while(self.head is not None):
                print(self.head.data,"-> ",end="")
                self.head = self.head.next
                
                
                
    #Insert a node in beginning
    def insert_beg(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new
        
        
        
    #Insertion at the end
    def insert_end(self,data):
        new = Node(data)
        
        if self.head is None:
            self.head = new
            
        #otherwise
        temp = self.head
        
        while(temp.next is not None):
            temp = temp.next
            temp.next = new
            new.next = None
            
            
    
    #insertion at any position
    def insert_any(self,data,position):
        new = Node(data)
        temp = self.head
        
        if self.head is None:
            self.head = new
          
        else:  
            i = 0
            while i < position - 1:
                temp = temp.next
                i = i + 1
            
            new.next = temp.next
            temp.next = new
        
        
        
        
    #deletion at beginning
    def delete_beg(self):
        
        if self.head is None:
            print("Linkedlist is Empty")
            
        else:
            self.head = self.head.next
           
           
           
    #deletion at the end
    def delete_end(self):
        
        if self.head is None:
            print("Linkedlist is Empty Can't delete")
            
        else:
            temp = self.head
            while(temp.next.next is not None):
                temp = temp.next
                
            temp.next = None
            
            
            
    #deletion by value
    def delete_value(self,value):
        if self.head is None:
            print("Cannot Delete, List is Empty")
            
        if value==self.head.data:
            self.head = self.head.next
            
        else:
            temp = self.head
            while(temp.next is not None):
                if temp.data == value:
                    break
                else:
                    temp = temp.next
                    
                    
            if temp.next is None:
                print("Item Not Found")
            else:
                temp.next = temp.next.next
                
                
                
    #reverse linkedlist
    def reverse(self):
        previous  = None
        current = self.head
        
        while(current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        
        self.head = previous
        
        
        
#Driver - Code        
linkedlist  = Linkedlist()
linkedlist.insert_beg(34)
linkedlist.insert_beg(45)
linkedlist.insert_end(87)
linkedlist.delete_value(45)         #delete by value
linkedlist.delete_beg()             #delete at beginning
linkedlist.insert_beg(23)

linkedlist.insert_beg(67)
linkedlist.delete_end()             #delete at end
linkedlist.insert_any(44,2)

#before = 67 -> 23 -> 44

linkedlist.reverse()

linkedlist.traversal()




        
        

    