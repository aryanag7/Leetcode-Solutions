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
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # Head of linked list

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  # Point new node to current top
        self.top = new_node       # Update top to new node

    def pop(self):
        if self.top is None:
            return None  
        popped_data = self.top.data
        self.top = self.top.next  # Move top pointer down
        return popped_data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)


s.print_stack()  # Output: 30 -> 20 -> 10 -> None

print("Top element:", s.peek())  # 30

print("Popped:", s.pop())         # 30
s.print_stack()                   # 20 -> 10 -> None
