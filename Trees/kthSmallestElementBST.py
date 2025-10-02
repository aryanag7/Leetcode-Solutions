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
    
    def inOrder_traversal(self,root,arr):
        if root is None:
            return 
        self.inOrder_traversal(root.left,arr)
        arr.append(root.val)
        self.inOrder_traversal(root.right,arr)



    #REMOVED THE extra space complexity by maintaining a counter
    #can also do reverse of inorder
    # RIGHT ROOT LEFT. -same counter logic
    def inOrder_traversal(self,root,count, k):
        if root is None:
            return None
        
        l = self.inOrder_traversal(root.left,count,k)

        count[0]+=1
        if count[0] == k:
            return root.val
        
        r = self.inOrder_traversal(root.right,count,k)

        if l is not None:
            return l
        else:
            return r
    


    # TC:- O(logN) - worst case N skewed
    # SC:- O(LogN) + O(N)
    
    def kthSmallest(self, root, k):
        arr = []
        return self.inOrder_traversal(root,[0],k)

        # return arr[k-1]

    


        
    
s1= Solution()
root = s1.take_input()
print(s1.kthSmallest(root,1))




