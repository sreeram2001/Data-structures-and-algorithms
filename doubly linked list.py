
#Doubly Linked list

class Node:
    
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data = data
        
        
class doublylinkedlist:
    
    def __init__(self):
        self.head = None
        
        
    #insertion before head
    def insertbeg(self,data):
        node = Node(data)
        
        if self.head == None:
            self.head = node
            
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            
            
            
    #insertion at the end        
    def insertend(self,data):
        node = Node(data)
        
        if self.head == None:
            self.head = node
            
        else:
            temp = self.head
            
            while temp.next is not None:
                temp = temp.next
                
            temp.next = node
            node.prev = temp
            node.next = None
            
            
            
    #inserting at any position
    def insertany(self,pos,data):
        node = Node(data)
        temp = self.head
        
        if self.head == None:
            self.head = node
            
        else:
            i = 0
            while i < pos-1:
                i = i + 1
                temp = temp.next
                
            temp_next = temp.next
            
            node.prev = temp
            node.next = temp.next
            temp_next.prev = node
            temp.next = node
            
            
    
    #deletion-front
    def deletebeg(self):
        
        if self.head is None:
            print("Doubly Linked LIst is Empty")
            
        else:
            self.head = self.head.next
            self.head.prev = None
            
            
            
    #deletion-end
    def deleteend(self):
        
        if self.head is None:
            print("Linked List is Empty")
            
        else:
            temp = self.head
            
            while temp.next.next != None:
                temp = temp.next
                
            temp.next = None
            
            
    #deletion-value
    def deleteval(self,value):
        
        if self.head is None:
            print('Empty List')
            
        else:
            temp = self.head
            
            while temp.next is not None:
                if temp.next.data == value:
                    break
                temp = temp.next
                
            
            nxt_item = temp.next.next
            nxt_item.prev = temp
            temp.next = temp.next.next
            
            
            
     
    #traversing - printing elements
    def traversalforw(self):
        
        if self.head is None:
            print("Empty")
            
        else:

            while self.head != None:
                print(self.head.data)
                self.head = self.head.next
                
                
                
                
    #traversing - backwards
    def traversalback(self):
        
        if self.head is None:
            print("Empty")
            
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
                
                
            while temp != None:
                print(temp.data)
                temp = temp.prev
                
                
                
                
    #reverse
    def reverse(self):
        temp = None
        curr = self.head
        
        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
            
        if temp is not None:
            self.head = temp.prev

    
#DRIVER CODE

dll = doublylinkedlist()

#insertion
dll.insertbeg(40)               #40
dll.insertend(50)               #40 -> 50
dll.insertend(60)               #40 -> 50 -> 60
dll.insertbeg(45)               #45 -> 40 -> 50 -> 60
dll.insertany(2,78)             #45 -> 40 -> 78 -> 50 -> 60
dll.insertany(4,100)            #45 -> 40 -> 78 -> 50 -> 100 -> 60


#deletion
dll.deletebeg()                 #40 -> 78 -> 50 -> 100 -> 60
dll.deleteend()                 #40 -> 78 -> 50 -> 100
dll.deleteval(50)               #40 -> 78 -> 100


#reverse traversal
dll.traversalback()             #100 -> 78 -> 40 

dll.reverse()                   #100 -> 78 -> 40
dll.traversalforw()             #after reversal