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

    # TC:- O(N)
    # SC: O(N)
    def maxDepth(self, root):
        # queue = deque([root])
        # max_level = 0

        # while len(queue)>0:
        #     n = len(queue)

        #     for i in range(0,n):
        #         node = queue.popleft()

        #         if node.left:
        #             queue.append(node.left)

        #         if node.right:
        #             queue.append(node.right)
            
        #     max_level = max(max_level, max_level+1)
        
        # return max_level
    
        """
        Diff is that you can avoid the for loop by just storing the level with the node but the TC is same
        """
        queue = deque([(root,1)])
        max_level = 1

        while len(queue)>0:
            node , level = queue.popleft()
            max_level = max(max_level, level)

            if node.left:
                queue.append((node.left,level+1))
            
            if node.right:
                queue.append((node.right,level+1))
        
        
        return max_level
    

    

s1= Solution()
root = s1.take_input()
print(s1.maxDepth(root))





        
        