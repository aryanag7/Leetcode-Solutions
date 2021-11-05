# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self,root):
        if root==None:
            return 0,True
        left_height,left_bal=self.help(root.left)
        right_height,right_bal=self.help(root.right)
        height=max(left_height,right_height)+1
        if abs(left_height-right_height)>1:
            return height,False
    
        if left_bal and right_bal:
            return height,True
        else:
            return height,False
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height,isbal=self.help(root)
        return isbal
        
    
        
