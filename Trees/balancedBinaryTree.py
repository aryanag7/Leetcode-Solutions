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
    

    def height_of_tree(self,root):
        if root is None:
            return 0

        left = self.height_of_tree(root.left)
        right = self.height_of_tree(root.right)

        return max(left,right)+1
    

    # TC:- O(N*N) because for every node, im calling height tree function to calculate height for n-1 nodes
    # SC:- O(N) stack space
    def isBalanced(self, root):
        if root is None:
            return True
        
        left_height = self.height_of_tree(root.left)
        right_height = self.height_of_tree(root.right)

        if abs(left_height-right_height)>1:
            return False
        
        if self.isBalanced(root.left)==False:
            return False
        
        if self.isBalanced(root.right)==False:
            return False

        return True
    


    # TC:- O(N)
    # SC:- O(N)
    #doing all the calculations of height of tree and checking for balanced or not while coming back from the base case
    def check_balanced_tree(self,root):
        if root is None:
            return 0,True
        
        left_height, left_balanced = self.check_balanced_tree(root.left)
        right_height, right_balanced = self.check_balanced_tree(root.right)

        new_height = max(left_height,right_height)+1

        if abs(right_height-left_height)>1:
            return new_height,False
        
        if not left_balanced:
            return new_height,False
        
        if not right_balanced:
            return new_height,False
        
        return new_height, True
    def isBalanced2(self, root):
        if root is None:
            return True
        
        height, isBalanced = self.check_balanced_tree(root)
        return isBalanced
        



s1= Solution()
root = s1.take_input()
print(s1.isBalanced2(root))



