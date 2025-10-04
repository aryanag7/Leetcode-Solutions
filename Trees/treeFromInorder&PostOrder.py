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
    

    def buildTreeHelper(self,postorder, inorder, postSt, postEnd, inSt, inEnd,inorder_index):

        if inSt > inEnd:
            return None
        
        rootValue = postorder[postEnd]

        root = TreeNode(rootValue)

        # index = None
        # for i in range(inSt, inEnd+1):
        #     if inorder[i] == rootValue:
        #         index = i
        #         break

        index = inorder_index[rootValue]

        l = index - inSt
        
        root.left  = self.buildTreeHelper(postorder, inorder, postSt, postSt+l-1, inSt, index-1,inorder_index)

        root.right  = self.buildTreeHelper(postorder, inorder, postSt+l, postEnd-1, index+1, inEnd,inorder_index)

        return root



    # TC:- O(N*N)- as for every recursive call searching in inorder 
    #optimized using hashmap O(N)
    # SC:- O(N) - stack space and O(N) hashmap to store index of every value of inorder
    def buildTree(self, postorder, inorder):
        inorder_index = { val:i for i,val in enumerate(inorder)}

        postSt, postEnd, inSt, inEnd = 0, len(postorder)-1, 0, len(inorder)-1

        return self.buildTreeHelper(postorder, inorder, postSt, postEnd, inSt, inEnd,inorder_index)

    
    def preorder_traversal(self,root):
        if root is None:
            print("None",end=" ")
            return
        
        print(root.val,end=" ")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)


        

    


        
    
s1= Solution()
# root = s1.take_input()
inorder = [40,20,50,10,60,30]
postorder = [40,50,20,60,30,10]
root = s1.buildTree(postorder, inorder)
s1.preorder_traversal(root)




