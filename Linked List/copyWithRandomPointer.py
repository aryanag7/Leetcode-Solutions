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

    # TC:- O(N)
    # SC:- O(N)
    def copyRandomList(self, head):
        randomMap={None:None}
        
        p=head
        while p:
            randomMap[p]=ListNode(p.val)
            p=p.next

        p=head
        while p:
            randomMap[p].next = randomMap[p.next]
            randomMap[p].random = randomMap[p.random]
            p=p.next
            
        return randomMap[head]



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
# head1=s1.take_input()
# head2=s1.take_input()
# new_head = s1.mergeTwoLists(head1,head2)
# s1.printLL(new_head)



