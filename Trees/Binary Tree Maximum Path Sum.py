# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self,root,maxi):
        if root==None:
            return 0
        left=max(0,self.help(root.left,maxi))
        right=max(0,self.help(root.right,maxi))

        maxi[0]=max(maxi[0],left+right+root.val)
        return root.val+max(left,right)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=[root.val]
        self.help(root,maxi)
        return maxi[0]
        
        
