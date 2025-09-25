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
        
        left_height = self.height_of_tree(root.left)
        right_height = self.height_of_tree(root.right)

        return max(left_height,right_height)+1
    
    # TC:- O(N*N)- same as balanced binary tree, calling height which is taking another O(N)
    # SC:- O(N)
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        
        left_height = self.height_of_tree(root.left)
        right_height = self.height_of_tree(root.right)

        along_root = left_height + right_height

        left_diam = self.diameterOfBinaryTree(root.left)
        right_diam = self.diameterOfBinaryTree(root.right)

        return max(left_diam, right_diam, along_root)
    


    # TC:- O(N)- same as balanced binary tree, computed height and diameter on the fly while coming back from base case
    # SC:- O(N)
    def diameterOfBinaryTree2(self, root):
        if root is None:
            return 0,0
        
        left_height,left_diam = self.diameterOfBinaryTree2(root.left)
        right_height, right_diam = self.diameterOfBinaryTree2(root.right)

        new_height  = max(left_height,right_height)+1

        new_diam = max(left_diam, right_diam, left_height+right_height)

        return new_height,new_diam






      




s1= Solution()
root = s1.take_input()
print(s1.diameterOfBinaryTree2(root))




