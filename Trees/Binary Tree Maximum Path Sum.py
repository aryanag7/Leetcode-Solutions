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
    


    
    def maxPathSumHelper(self,root, maxi):
        if root is None:
            return 0
        
        left_sum = self.maxPathSumHelper(root.left,maxi)
        right_sum = self.maxPathSumHelper(root.right,maxi)

        maxi[0] = max(maxi[0], root.val+ left_sum+ right_sum)

        return root.val + max(left_sum,right_sum)
    

    # TC:- O(N)
    # SC:- O(N)
    def maxPathSum(self, root):
        maxi = [float('-inf')]

        self.maxPathSumHelper(root,maxi)

        return maxi[0]




    
s1= Solution()
root = s1.take_input()
print(s1.maxPathSum(root))




