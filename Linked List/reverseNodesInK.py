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

    #TC:- O(N), each node is processed once. There are N/K groups and work done in each group is K so k * N/K = O(N)
    # SC:- O(N/K) Recursion Stack Space
    def reverseKGroup(self, head,k):
        if head is None:
            return None
        curr=head
        countNodes = 0

        while curr:
            countNodes+=1
            curr=curr.next
        
        if countNodes<k:
            return head
        
        prev=None
        curr=head
        i=0
        while countNodes>=k and i<k:
            forward=curr.next
            curr.next=prev
            prev=curr
            curr=forward
            i+=1
        
        newHead= prev
        reversedHead= self.reverseKGroup(curr,k)

        head.next= reversedHead

        return newHead


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
new_head = s1.reverseKGroup(head,3)
s1.printLL(new_head)



