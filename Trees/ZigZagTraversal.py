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
    
    # TC:- O(N)+O(N) ( for popping in for loop max n nodes)
    # SC:- O(N) + O(N)
    # can also use n-i-1 formula to place starting from 0th index to last index 0->n-1, 1-> n-2
    def zigzagLevelOrder(self, root):
        queue = [root]
        ans= []
        flag = True
        while len(queue)>0:
            n = len(queue)
            level = []
            for i in range(0,n):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            if flag:
                ans.append(level)
            else:
                ans.append(level[::-1])

            flag  = not(flag)

        return ans

    
    
s1= Solution()
root = s1.take_input()
print(s1.zigzagLevelOrder(root))




