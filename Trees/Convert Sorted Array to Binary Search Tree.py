# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return 
        mid=len(nums)//2

        root=TreeNode(nums[mid])

        left_tree=self.sortedArrayToBST(nums[0:mid])

        right_tree=self.sortedArrayToBST(nums[mid+1:])

        root.left=left_tree
        root.right=right_tree

        return root

