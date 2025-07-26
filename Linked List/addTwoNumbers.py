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

    # TC:- O(MAX(LEN(L1),LEN(L2)))
    def addTwoNumbers(self,l1,l2):
        carry=0
        dummyNode = ListNode(-1)
        curr=dummyNode
        while l1 or l2 or carry:
            s=0
            if l1 is not None:
                s+=l1.val
                l1=l1.next

            if l2 is not None:
                s+=l2.val
                l2=l2.next
            
            s+=carry

            carry=s//10

            newNode = ListNode(s%10)
            curr.next=newNode
            curr=curr.next

        return dummyNode.next
    

    
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
head1=s1.take_input()
head2=s1.take_input()
new_head = s1.addTwoNumbers(head1,head2)
s1.printLL(new_head)



