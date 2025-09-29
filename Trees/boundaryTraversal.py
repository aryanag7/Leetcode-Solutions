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
    
    def left_boundary_traversal(self,root, left_boundary):
        if root is None or root.left is None and root.right is None:
            return 
        
        left_boundary.append(root.val)
        
        if root.left:
            self.left_boundary_traversal(root.left, left_boundary)
        else:
            self.left_boundary_traversal(root.right, left_boundary)
    
    def leaf_nodes_traversal(self, root, leaf_nodes):
        if root is None:
            return 
        if root.left is None and root.right is None:
            leaf_nodes.append(root.val)
            return
        
        self.leaf_nodes_traversal( root.left, leaf_nodes)

        self.leaf_nodes_traversal( root.right, leaf_nodes)


    def right_boundary_traversal(self, root, right_boundary):
        if root is None or root.left is None and root.right is None:
            return 
        
        right_boundary.append(root.val)
        
        if root.right:
            self.right_boundary_traversal(root.right, right_boundary)
        else:
            self.right_boundary_traversal(root.left, right_boundary)
    



    # TCL- O(N) + O(N) + O(N) - 3N , assume skewed tree only left left, or only right right
    # SC:- O(N)
    def boundaryOfBinaryTree(self, root):
        if root is None:
            return None

        if root.left is None and root.right is None:
            return [root.val]
        
        ans = [root.val]

       
        self.left_boundary_traversal(root.left, ans)


        self.leaf_nodes_traversal(root, ans)

        right_boundary = []
        self.right_boundary_traversal(root.right, right_boundary)

        right_boundary = right_boundary[::-1]


        ans.extend(right_boundary)

        return ans
   



    
    
s1= Solution()
root = s1.take_input()
print(s1.boundaryOfBinaryTree(root))




