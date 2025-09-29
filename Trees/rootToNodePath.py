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
    

    #ROOT TO TARGRT NODE PATH
    def Dfs_helper(self,root, node, path):
        if root is None:
            return False
        
        if root.val == node:
            path.append(root.val)
            return True
        
        left = self.Dfs_helper(root.left, node, path)

        if not left:
            right = self.Dfs_helper(root.right, node, path)

        right = False
        if left or right:
            path.append(root.val)
            return True
        
        return False
        
    def rootToNodePath(self,root, node):
        path =[]
        self.Dfs_helper(root,node, path)

        return path[::-1]
    



    # TC:- O(N)
    # SC:- O(N)
    def Dfs_paths_helper(self, root, path ,ans):
        if root is None:
            return 
        
        if root.left is None and root.right is None:
            path.append(root.val)
            s = "->".join(map(str,path))
            ans.append(s)
            path.pop()
            return 

        path.append(root.val)

        self.Dfs_paths_helper(root.left, path ,ans)


        self.Dfs_paths_helper(root.right, path ,ans)

        path.pop()

        


    def binaryTreePaths(self, root):
        ans=[]
        self.Dfs_paths_helper(root,[],ans)
        return ans


        



 
    
s1= Solution()
root = s1.take_input()
print(s1.binaryTreePaths(root))




