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


    # TC:- O(N+N/2)
    # SC:- O(1)
    # def middleOfLL(self, head):
    #     if head is None or head.next is None:
    #         return head
    #     count=0
    #     p=head

    #     while p:
    #         count+=1
    #         p=p.next
        
    #     mid=count//2

    #     p=head
    #     i=0
    #     while i<mid:
    #         p=p.next
    #         i+=1
        
    #     return p.val


    #Single pass TC:- O(N)
    # SC:- O(1)
    def middleOfLL(self, head):
        p=head
        q=head

        while q and q.next:
            p=p.next
            q=q.next.next
        
        return p.val


        

    
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
print(s1.middleOfLL(head))
# s1.printLL(reversed_head)



