# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self,root,ans,bool):
        if root==None:
            return
   
        self.help(root.left,ans,True)
        if bool and  root.left==None and root.right==None:
            ans[0]=ans[0]+root.val
    
        self.help(root.right,ans,False)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        self.help(root,ans,False)
        return ans[0]
        
        
