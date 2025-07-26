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
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        
        curr=head
        forward=curr
        prev=None

        while curr is not None:
            forward=curr.next
            curr.next=prev
            prev=curr
            curr=forward

        
        head=prev
        return head
    
    def middleOfLL(self, head):
        p=head
        q=head

        while q and q.next:
            p=p.next
            q=q.next.next
        
        return p
    
    def reorderList(self, head):
        middleNode= self.middleOfLL(head)
        reversedHead= self.reverseList(middleNode.next)
        middleNode.next=None


        first=head
        second=reversedHead

        while second:
            t1=first.next
            first.next=second
            first= t1

            t2=second.next
            second.next = first
            second=t2
        
        return head


    
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
newHead = s1.reorderList(head)
s1.printLL(newHead)



