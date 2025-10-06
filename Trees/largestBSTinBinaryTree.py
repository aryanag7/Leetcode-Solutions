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
    

    
    def isValidBSTHelper(self,root, largest):
        if root is None:
            return float('-inf'), float('inf'), True,0
        
        left_max, left_min, left_balanced, left_nodes = self.isValidBSTHelper(root.left,largest)

        right_max, right_min, right_balanced , right_nodes= self.isValidBSTHelper(root.right,largest)

        new_max = max(root.val, left_max, right_max)
        new_min = min(root.val, left_min, right_min)

        if left_max >= root.val  or right_min <= root.val:
            return new_max, new_min, False,left_nodes+right_nodes+1

        if left_balanced and right_balanced:
            largest[0] = max(largest[0], left_nodes+right_nodes+1)

            return new_max, new_min, True,left_nodes+right_nodes+1

        return new_max, new_min, False,left_nodes+right_nodes+1


    def isValidBST(self, root):
        if root is None:
            return 0

        largest = [0]
        
        maxi, mini, isBalanced, total_nodes = self.isValidBSTHelper(root, largest)

        return largest[0]
    

    
s1= Solution()
root = s1.take_input()
print(s1.isValidBST(root))




