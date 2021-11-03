# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        left_child=self.maxDepth(root.left)
        right_child=self.maxDepth(root.right)
        return max(left_child,right_child)+1
        
