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

    def preOrder_traversal(self,root,subRoot):
        if root is None or subRoot is None:
            return root == subRoot
        
        if root.val != subRoot.val:
            return False

        left = self.preOrder_traversal(root.left, subRoot.left)
        right = self.preOrder_traversal(root.right, subRoot.right)

        return left and right
       

    # TC:- O(M*N) as for eery node in big tree, calling a function to match with the subtree which is O(N)
    # SC:- O(N) + O(N)
    def isSubtree(self, root, subRoot):
        stack = [root]
        while len(stack)>0:
            node = stack.pop()
            isMatched = self.preOrder_traversal(node,subRoot)
            if isMatched:
                return True


            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        
        return False
    






    def preOrder_traversal_optimized(self,root,s):
        if root is None:
            s.append("N")
            return 

        
        # "(3)"
        s.append(f"({root.val})") 


        self.preOrder_traversal_optimized(root.left, s)
        self.preOrder_traversal_optimized(root.right,s)

      
    # TC:- O(N) + O(M) + O(N+M)
    # SC:- O(N) + O(M)
    
    def isSubtreeOptimized(self, root, subRoot):
        rootString = []
        self.preOrder_traversal_optimized(root,rootString)


        subRootString = []
        self.preOrder_traversal_optimized(subRoot,subRootString)


        return  "".join(subRootString) in "".join(rootString)


 


    




    
s1= Solution()
root = s1.take_input()
subRoot = s1.take_input()
print(s1.isSubtreeOptimized(root,subRoot))




