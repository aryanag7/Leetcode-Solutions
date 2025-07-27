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

class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.key=key
        self.value=value

# TC:- O(1) as its just link changes, hashmap
# SC:- DLL O(capacity of nodes) , Hashmap O(capacity of nodes)

class LRUCache:

    def __init__(self, capacity: int):
        self.nodeMap={}
        self.dummyHead= Node(-1,-1)
        self.dummyTail = Node(-1,-1)
        
        self.dummyHead.next= self.dummyTail
        self.dummyTail.prev= self.dummyHead

        self.capacity = capacity
    
    def removeHelper(self,node):
        node.prev.next= node.next
        node.next.prev = node.prev
 
    def insertAtFront(self,node):
        #node connections
        node.next=self.dummyHead.next
        node.prev=self.dummyHead

        self.dummyHead.next.prev= node
        self.dummyHead.next= node

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node= self.nodeMap[key]
        self.removeHelper(node)
        self.insertAtFront(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node=self.nodeMap[key]
            self.removeHelper(node)
            node.value= value
            self.insertAtFront(node)
        else:
            if len(self.nodeMap)==self.capacity:
                self.nodeMap.pop(self.dummyTail.prev.key)
                self.dummyTail.prev=self.dummyTail.prev.prev
                self.dummyTail.prev.next=self.dummyTail

            newNode= Node(key, value)
            self.nodeMap[key]= newNode
            self.insertAtFront(newNode)


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)