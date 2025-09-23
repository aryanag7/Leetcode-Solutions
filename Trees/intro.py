import bisect
import sys
import os
import math
from collections import defaultdict
from collections import Counter
from typing import Deque
from collections import deque
from itertools import accumulate
import heapq

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Redirect stdin and stdout
sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def take_input():
    root_data=int(input())
    if root_data==-1:
        return None
    

    root=BinaryTreeNode(root_data)

    root.left= take_input()

    root.right= take_input()

    return root



root = take_input()

#DFS Traversals

# TC:- O(N)
# SC:- O(N)

def preorder(node):
    if node is None:
        return
    print(node.data, end=' ')

    preorder(node.left)

    preorder(node.right)


def inorder(node):
    if node is None:
        return
    
    inorder(node.left)

    print(node.data, end=' ')

    inorder(node.right)



def postorder(node):
    if node is None:
        return
    
    postorder(node.left)

    postorder(node.right)

    print(node.data, end=' ')


#BFS- Level order traversal

# TC:- O(N)
# SC:- O(N)
def level_order_traversal(root):
    if root is None:
        return []
    queue = deque([root])
    maxLevel = 0
    level = 1

    ans=[]

    while len(queue)>0:
        n = len(queue)
        level = []
        for i in range(0,n):
            node = queue.popleft()
            print(node.data, end=" ")
            level.append(node.data)
        
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            
        print()
        maxLevel = max(maxLevel, maxLevel+1)
        ans.append(level)
    
    print(maxLevel)
    print(ans)




level_order_traversal(root)