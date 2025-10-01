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
    
    def find_parents(self,root, parent, parent_map):
        if root is None:
            return
        
        
        parent_map[root] = parent

        self.find_parents(root.left, root, parent_map)
        

        self.find_parents(root.right, root, parent_map)


    def find_nodes_at_k_level(self, root, parent_map, curr_level, k, visited, ans):
        if root is None or root in visited:
            return 
        
        visited.add(root)
        
        if curr_level == k:
            ans.append(root.val)
            return 
        
        p = parent_map[root]
        if p is not None:
            self.find_nodes_at_k_level(p, parent_map, curr_level+1, k, visited, ans)

        self.find_nodes_at_k_level(root.left, parent_map, curr_level+1, k, visited, ans)

        self.find_nodes_at_k_level(root.right, parent_map, curr_level+1, k, visited, ans)



    # TC:- O(N)+ O(N)
    # SC:- O(N)+O(N)
    def distanceK(self, root, target, k):
        parent_map = {}
        self.find_parents(root, None, parent_map)
        print(parent_map)

        ans = []
        visited = set()
        self.find_nodes_at_k_level(target, parent_map, 0, k, visited,ans)

        return ans
        

        
    
s1= Solution()
root = s1.take_input()
print(s1.distanceK(root, 5, 2))




