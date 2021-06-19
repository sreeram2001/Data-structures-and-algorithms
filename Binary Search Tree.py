
#Binary Search Tree

class BST:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
    #insertion   
    def insert(self,data):
        if data==self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
                
        if data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
            

    #search            
    def search(self,value):
        if self.data == value:
            return True
            
        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False
                
        if val > self.data:
            if self.right:
                self.right.search(val)
            else:
                return False
    
    
    #Print Inorder Traversal
    def print_inorder(self):
        ele = []
        
        if self.left:
            ele = ele + self.left.print_inorder()
            
        ele.append(self.data)
        
        if self.right:
            ele = ele + self.right.print_inorder()

        return ele

            
#Driver Code:

root = BST(50)
root.insert(40)
root.insert(34)
root.insert(60)
root.insert(45)

print(root.print_inorder())
            
    
