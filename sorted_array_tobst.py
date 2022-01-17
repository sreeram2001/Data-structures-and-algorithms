# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        root = self.bst(nums,0,len(nums)-1)
        return root

    def bst(self,nums,left,right):
        if left < right:
            mid = (left+right)//2
            
            nodes = TreeNode(nums[mid])
            nodes.left = self.bst(nums,left,mid-1)
            nodes.right = self.bst(nums,mid+1,right)
            
            return nodes
        
        elif left == right:
            nodes = TreeNode(nums[left])
            return nodes
        
        else:
            return None
        
 
