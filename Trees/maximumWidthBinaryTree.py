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
    

    # def widthOfBinaryTree(self, root):
    #     queue = deque([root])
    #     ans = float('-inf')
    #     while len(queue)>0:

    #         n=len(queue)
    #         left = None
    #         right = None
    #         for i in range(0,n):
    #             node = queue.popleft()

    #             if node!=None:
    #                 if left is None:
    #                     left = i
    #                 right = i

    #             else:
    #                 queue.append(None)
    #                 queue.append(None)
    #                 continue

    #             if node.left:
    #                 queue.append(node.left)
    #             else:
    #                 queue.append(None)
                
    #             if node.right:
    #                 queue.append(node.right)
    #             else:
    #                 queue.append(None)
            
    #         if left is None and right is None:
    #             break
            
    #         ans = max(ans, right-left+1)
        
    #     return ans



    #rather than going at every level and getting non null left and right indexes everytime, start with index 1 root node and then go down with the neew indexes
    # TC:- O(N)
    # SC:- O(N)
    def widthOfBinaryTree(self, root):
        queue = deque([(root,1)])

        ans = 0

        while len(queue)>0:
            n=len(queue)
            l = queue[0][1]
            r = queue[-1][1]
            for i in range(0,n):
                node, index = queue.popleft()

                if node.left:
                    queue.append((node.left,2*index))
                
                if node.right:
                    queue.append((node.right,2*index+1))
            
            #level finished
            ans = max(ans, r-l+1)
        
        return ans            
    
s1= Solution()
root = s1.take_input()
print(s1.widthOfBinaryTree(root))




