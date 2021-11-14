# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        queue = []
        if root is None:
            return 
        
        queue.append(root)
        while queue:
            l = len(queue)
            
            while l > 0:
                l = l - 1
                
                curr = queue.pop(0)
                
                if l==0:
                    arr.append(curr.val)
                    
                if curr.left:
                    queue.append(curr.left)
                    
                if curr.right:
                    queue.append(curr.right)
                    
        return arr
