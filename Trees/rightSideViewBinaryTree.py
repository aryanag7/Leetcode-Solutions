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
    
    # TC:- O(N)+O(N)
    # SC:- O(N)
    def rightSideView(self, root):
        queue = deque([root])
        ans = []
        
        while len(queue)>0:
            n = len(queue)
            ans.append(queue[-1].val)

            for i in range(0,n):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
        return ans
    

    #recursive way of doing this , travresing on right first and checking if a new level is reached or not
    def right_view(self,root,ans,level,max_level):
        if root is None:
            return

        if level>max_level[0]:
            ans.append(root.val)
            max_level[0]=level
            
        self.right_view(root.right,ans,level+1,max_level)
  
        self.right_view(root.left,ans,level+1,max_level)


    def rightSideView(self, root):
        ans=[]
        self.right_view(root,ans,0,[float('-inf')])
        return ans

    
 
    
s1= Solution()
root = s1.take_input()
print(s1.rightSideView(root))




