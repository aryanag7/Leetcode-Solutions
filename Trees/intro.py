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



# Preorder, Inorder, Postorder - Iterative


#Iterative Preorder using Stack
#TC:- O(N)
#SC:- O(N) ~ O(height) if skewed tree
def iterative_preorder(root):
    stack = [root]
    preorder = []
    while len(stack)>0:
        node = stack.pop()
        preorder.append(node.data)

        if node.right:
            stack.append(node.right)
        

        if node.left:
            stack.append(node.left)
    
    return preorder



#Iterative Inorder using Stack
#TC:- O(N)
#SC:- O(N) ~ O(height) if skewed tree
def iterative_inorder(root):
    stack = []
    inorder = []
    node = root

    while True:
        if node is not None:
            stack.append(node)
            node = node.left
        
        else:
            if len(stack)==0:
                break
            ele = stack.pop()
            inorder.append(ele.data)

            node = ele.right
    
    return inorder
    

    

#Iterative Postorder using 2 Stacks
#TC:- O(N)
#SC:- O(N) + O(N) 
def iterative_postorder(root):
    stack1= [root]
    stack2 = []

    while len(stack1)>0:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        
        if node.right:
            stack1.append(node.right)
    
    postorder = []

    while len(stack2)>0:
        postorder.append(stack2.pop().data)
    

    return postorder



#Iterative Postorder using 1 Stack
# Postorder is Left Right Root - do the opposite Root Right Left and reverse it
#TC:- O(N)
#SC:- O(N) 
def iterative_postorder_oneStack(root):
    stack = [root]
    postorder = []

    while len(stack)>0:
        node  = stack.pop()
        postorder.append(node.data)


        if node.left:
            stack.append(node.left)
        
        if node.right:
            stack.append(node.right)
    
    postorder.reverse()

    return postorder






#Preorder, Inorder, Postorder all in 1 go (RECURIVE)
# TC:- O(N)
# SC:- O(3N) + N STACK SPACE
def all_traversals_recursive(root):

    def recurse_all_traversals(root,pre,ino,post):
        if root is None:
            return 
        
        pre.append(root.data)


        recurse_all_traversals(root.left,pre,ino,post)

        ino.append(root.data)

        recurse_all_traversals(root.right,pre,ino,post)

        post.append(root.data)


    
    pre = []
    ino = []
    post = []
    recurse_all_traversals(root,pre, ino, post)

    print(pre)
    print(ino)
    print(post)






#Preorder, Inorder, Postorder all in 1 go (iterative)
# TC:- O(3N)
# SC:- O(3N)
def all_traversals_iterative(root):

    stack = [(root,1)]
    preorder = []
    inorder = []
    postorder = []

    while len(stack)>0:
        node,count = stack.pop()

        if count == 1:
            preorder.append(node.data)
            stack.append((node,count+1))

            if node.left:
                stack.append((node.left,1))

        
        elif count == 2:
            inorder.append(node.data)
            stack.append((node,count+1))

            if node.right:
                stack.append((node.right,1))
                
        else:
            postorder.append(node.data) 
    
    print(preorder)
    print(inorder)
    print(postorder)



all_traversals_iterative(root)