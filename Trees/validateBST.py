import bisect
import sys
import os
import math
from collections import defaultdict
from collections import Counter
from typing import Deque
from collections import deque
from itertools import accumulate

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Redirect stdin and stdout
sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def take_input(self):
        root_data=int(input())
        if root_data==-1:
            return None
        

        root=TreeNode(root_data)

        root.left= self.take_input()

        root.right= self.take_input()

        return root
    
    # def max_element(self,root):
    #     if root is None:
    #         return 0
        
    #     left = self.max_element(root.left)
    #     right = self.max_element(root.right)

    #     return max(left, right, root.val)
    

    # def min_element(self,root):
    #     if root is None:
    #         return float('inf')
        
    #     left = self.min_element(root.left)
    #     right = self.min_element(root.right)

    #     return min(left, right, root.val)
    

    # TC:- O(N*N) - as for every node you are calling another function to calculate the max and min from left and right then calling the function again for every subtree
    # SC:- O(N)
    # def isValidBST(self, root):
    #     if root is None:
    #         return True
        
    #     left_max = self.max_element(root.left)
    #     right_min = self.min_element(root.right)

    #     if left_max >= root.val and right_min <= root.val:
    #         return False
        
    #     left_isBST = self.isValidBST(root.left)
    #     right_isBST = self.isValidBST(root.right)

    #     if left_isBST and right_isBST:
    #         return True
    #     return False


    # ----- optimized approach -------
    # TC:- O(N), as we are calculating all the values max,min, isbal on the fly while coming back from the base case
    # SC:- O(N)
    def isValidBSTHelper(self,root):
        if root is None:
            return float('-inf'), float('inf'), True
        
        left_max, left_min, left_balanced = self.isValidBSTHelper(root.left)

        right_max, right_min, right_balanced = self.isValidBSTHelper(root.right)

        new_max = max(root.val, left_max, right_max)
        new_min = min(root.val, left_min, right_min)

        if left_max >= root.val  or right_min <= root.val:
            return new_max, new_min, False

        if left_balanced and right_balanced:
            return new_max, new_min, True

        return new_max, new_min, False


    def isValidBST(self, root):
        if root is None:
            return True
        
        maxi, mini, isBalanced = self.isValidBSTHelper(root)

        return isBalanced
    



    # ------ InOrder traversal always gives sorted arrays in BST ------
    
    # TC:- O(N)
    # SC:- O(N) + O(N)
    def inOrder_traversal(self, root,arr):
        if root is None:
            return 
        
        self.inOrder_traversal(root.left, arr)
        arr.append(root.val)
        self.inOrder_traversal(root.right, arr)

    
    def isValidBST(self, root):
        if root is None:
            return True
        arr = []
        self.inOrder_traversal(root,arr)

        if len(arr)==1:
            return True
        
        prev=0
        for i in range(1,len(arr)):
            if arr[i] <= arr[prev]:
                return False
            prev= i
        
        return True

        

        
    
s1= Solution()
root = s1.take_input()
print(s1.isValidBST(root))




