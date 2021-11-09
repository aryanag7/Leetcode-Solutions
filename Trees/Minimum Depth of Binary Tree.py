# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans=[]
        depth=1
        self.help(root,depth,ans)
        if len(ans)>0:
            return min(ans)
        else:
            return 0
    
        
        
    def help(self,root,depth,ans):
        if root==None:
            return None
        if root.left==None and root.right==None:
            ans.append(depth)
       
        
        self.help(root.left,depth+1,ans)
        self.help(root.right,depth+1,ans)

        
