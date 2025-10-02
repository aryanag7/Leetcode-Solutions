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
    

    def seriealize_helper(self, root,path):
        if root is None:
            path.append("N")
            return
        
        path.append(str(root.val))

        self.seriealize_helper(root.left,path)

        self.seriealize_helper(root.right,path)



    # TC:- O(N) to get the while data from tree
    # SC:- O(N) + O(N) - stack space plus space to store path
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        path = []

        self.seriealize_helper(root,path)

        s = ",".join(path)
        print(s)
        return s
        

    # TC:- O(N) - max tokens would be 2n+1 for n nodes
    # SC:- O(N)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        li = iter(data.split(","))

        def helper(root):

            val = next(li)

            if val == "N":
                return None
            
            root = TreeNode(int(val))


            root.left = helper(root)


            root.right = helper(root)

            return root

        return helper(root)
    
    # ------ CAN ALSO DO THIS USING INDEX VARIABLE -----
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        li = data.split(",")
        index = [0]

        def helper():

            val = li[index[0]]

            if val == "N":
                index[0]+=1
                return None
            
            root = TreeNode(int(val))
            index[0]+=1

            root.left = helper()


            root.right = helper()

            return root

        return helper()
    

    
    
    
    def preOrder_traversal(self, root):
        if root is None:
            print("None",end=" ")
            return
        
        print(root.val,end=" ")

        self.preOrder_traversal(root.left)

        self.preOrder_traversal(root.right) 

    


        
    
s1= Solution()
root = s1.take_input()
s= s1.serialize(root)
root = s1.deserialize(s)
s1.preOrder_traversal(root)
# print(s1(root))




