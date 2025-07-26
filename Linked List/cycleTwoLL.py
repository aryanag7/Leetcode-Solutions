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
    #SC:- O(N) to add the nodes
    def detectCycle(self, head):
        seen= set()
        p=head
        while p:
            if p not in seen:
                seen.add(p)
            else:
                return p
            p=p.next

        return None
    

    def hasCycle(self, head):
        if head is None or head.next is None:
            return False,None

        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True,slow
        return False,None

    #TC:- O(N)
    #SC:- O(1) 
    def detectCycle(self, head):
        hasCycle,meetingPoint = self.hasCycle(head)
        if not(hasCycle):
            return None
        
        p=head
        q=meetingPoint

        while p!=q:
            p=p.next
            q=q.next
        
        return p
    




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



