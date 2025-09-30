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
    

    # TC:- O(LOGN) - as we wont be traversing the whole tree, we may go right, left, right cut through the tree based on the condition
    # SC:- O(LOGN) - if balanced BST else O(N) if skewed

    def searchBST(self, root, val):
        if root is None:
            return None
        
        if val == root.val:
            return root
        
        elif val < root.val:
            return self.searchBST(root.left, val)
        
        else:
            return self.searchBST(root.right, val)
        
    
s1= Solution()
root = s1.take_input()
print(s1.searchBST(root,8))




