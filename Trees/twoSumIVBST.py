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



    def inorder_traversal(self,root,arr):
        if root is None:
            return
        
        self.inorder_traversal(root.left,arr)

        arr.append(root.val)

        self.inorder_traversal(root.right,arr)



    # TC:- O(N)+O(N)
    # SC: O(N) - stack space  and O(N) to store elements
    def findTarget(self, root, k):
        arr = []
        self.inorder_traversal(root,arr)

        i=0
        j= len(arr)-1

        while i<j:
            if arr[i] + arr[j] == k:
                return True
            
            elif arr[i] + arr[j] > k:
                j-=1
            
            else:
                i+=1
        
        return False

        
    
s1= Solution()
root = s1.take_input()
print(s1.findTarget(root, 9))




