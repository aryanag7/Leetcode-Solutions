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
    
    def Dfs_traversal(self, root,d,level,col, min_col, max_col):
        if root is None:
            return 
        
        d[col].append((level,root.val))
        min_col[0] = min(min_col[0], col)
        max_col[0] = max(max_col[0], col)
        
        self.Dfs_traversal(root.left ,d,level+1,col-1, min_col, max_col)           

        self.Dfs_traversal(root.right ,d,level+1,col+1, min_col, max_col)      

    
    # TC:- O(N) + MlogM - where M is max nodes stored for a particular column
    # SC:- O(N) + O(M) (temp)

    def verticalTraversal(self, root):
        d = defaultdict(list)

        min_col =[float('inf')]
        max_col = [float('-inf')]

        self.Dfs_traversal(root,d,0,0, min_col, max_col)

        ans = []

        for c in range(min_col[0], max_col[0]+1):
            li = d[c]

            col_values=[]
            sorted_li = sorted(li, key= lambda x:(x[0],x[1]))
            for l,val in sorted_li:
                col_values.append(val)
            
            ans.append(col_values)
        
        return ans

    
s1= Solution()
root = s1.take_input()
print(s1.verticalTraversal(root))




