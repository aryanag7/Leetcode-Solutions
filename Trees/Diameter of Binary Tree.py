# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        height,diameter=self.help(root)
        return diameter
    
    def help(self,root):
        if root==None:
            return 0,0
        left_height,left_diam=self.help(root.left)
        right_height,right_diam=self.help(root.right)
        height=max(left_height,right_height)+1
        return height,max(left_height+right_height,left_diam,right_diam)


        
