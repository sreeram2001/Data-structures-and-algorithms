
#Binary Search Tree - insert,max,min,inorder,deletion,search


class BinarySearchTree:
    
    
    #initialzie
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        
    
    
    #insertion
    def insert(self,data):
        
        if self.data:
            
            if data < self.data:                                 #left-subtree
                if self.left is None:
                    self.left = BinarySearchTree(data)
                else:
                    self.left.insert(data)
                    
                    
            if data > self.data:                                #right-subtree
                if self.right is None:
                    self.right = BinarySearchTree(data)
                else:
                    self.right.insert(data)
                    
        else:
            self.data = data                                    #root-node
            
            
     
     
    #minimum-value                              
    def minvalue(root):                             #left-most leaf
        
        while(root.left is not None):
            root = root.left
            
        return root.data
        
        
        
        
    #maximum-value
    def maxvalue(root):                           #rightmost - leaf
        
        while(root.right is not None):
            root = root.right
            
        return root.data
        
        
        
    #inorder
    def inorder(self):
        
        if self.left:                           #left
            self.left.inorder()
            
        print(self.data)                        #root
        
        if self.right:                          #right
            self.right.inorder()
    
    
    
    #pre-order
    def preorder(self):
        
        print(self.data)                        #root
        
        if self.left:                           #left
            self.left.preorder()
            
        if self.right:                          #right
            self.right.preorder()
    
        

    
    #post-order
    def postorder(self):
        
        if self.left:                       #left
            self.left.postorder()
            
        if self.right:                      #right
            self.right.postorder()
            
        print(self.data)                    #root
        
        
        
        
    #searching
    def search(self,data):
        
        if data < self.data:
            if self.left is None:
                return "Not Found"
            else:
                return self.left.search(data)
                
        elif data > self.data:
            if self.right is None:
                return "Not Found"
            else:
                return self.right.search(data)
                
        else:
            print(data,"Found At : ",self)

                        

#Driver - Code

bst = BinarySearchTree(40)
bst.insert(45)
bst.insert(34)
bst.insert(24)
bst.insert(60)

bst.search(45)
print("")


#Outputs
print("The inorder Traversal : ")
bst.inorder()

print("The Minimum Value: ",bst.minvalue())
print("the Maximum Value: ",bst.maxvalue(),"\n")


print("The pre-order traversal : ")
bst.preorder()

print("The post-order traversal : ")
bst.postorder()


                
        

    
    

