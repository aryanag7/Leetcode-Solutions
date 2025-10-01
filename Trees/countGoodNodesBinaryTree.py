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
    
    def findGoodNodes(self, root, currMax):
        if root is None:
            return 0
       
        left = 0
        if root.left:
            left = self.findGoodNodes(root.left, max(currMax, root.left.val))


        right =0
        if root.right: 
            right = self.findGoodNodes(root.right,  max(currMax, root.right.val))

        
        if currMax <= root.val:
            return left + right  + 1

        else:
            return left + right 

    # TC:- O(N)
    # SC: -O(N)
    def goodNodes(self, root):

        return self.findGoodNodes(root,root.val)

 
 

        
    
s1= Solution()
root = s1.take_input()
print(s1.goodNodes(root))




