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
    
    # TC:- O(N) - first node on each new col (width)
    # SC:- O(N) + ANS

    #Recursive approach doesnt work here cuz we can visit a deeper node first on left subtree at a column ch = 1 while the node closer to root with same level existing, so level order traversal as it visits closer to root
    def topView(self,root):
        d = {}
        min_col = float('inf')
        max_col = float('-inf')

        queue = deque([(root,0)])

        while len(queue)>0:
            node, col = queue.popleft()
            min_col = min(min_col,col)
            max_col = max(max_col,col)

            if col not in d:
                d[col] = node.val

            if node.left:
                queue.append((node.left,col-1))

            if node.right:
                queue.append((node.right,col+1))

        ans = []

        for i in range(min_col, max_col+1):
            ans.append(d[i])
        
        return ans

    
 
    
s1= Solution()
root = s1.take_input()
print(s1.topView(root))




