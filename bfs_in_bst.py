
#LEVEL ORDER TRAVERSAL IN BINARY SEARCH TREE

class BST:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

def bfs_traversal(root):
    if root is None:
        return
    
    q = []
    q.append(root)
    
    while len(q) > 0:
        
        print(q[0].data)
        curr = q.pop(0)
        
        if curr.left:
            q.append(curr.left)
            
        if curr.right:
            q.append(curr.right)

#user-code
bst = BST(1)
bst.left = BST(2)
bst.right = BST(3)
bst.left.left = BST(4)
bst.right.right = BST(5)
bfs_traversal(bst)

    