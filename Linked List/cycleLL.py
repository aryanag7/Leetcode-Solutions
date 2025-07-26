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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    #TC:- O(N)
    #SC:- O(N) to store nodes in a set or a map
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False

        seen = set()
        p=head
        while p:
            if p not in seen:
                seen.add(p)
            else:
                return True
            p=p.next
        
        return False
    
    #TC:- O(N)
    #SC:- O(1) 
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False

        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True
        return False

    def take_input(self):
        head=None
        tail=None

        arr=list(map(int,input().split(" ")))
        for ele in arr:
            if ele ==-1:
                break
            new_node= ListNode(ele)
            if head is None and tail is None:
                head=new_node
                tail=new_node
            else:
                tail.next= new_node
                tail=tail.next

        return head

    def printLL(self,head):
        curr=head
        while curr:
            print(curr.val,end=" -> ")
            curr=curr.next

        print('None')
    
    
s1= Solution()
head=s1.take_input()
new_head = s1.removeNthFromEnd(head,6)
s1.printLL(new_head)



