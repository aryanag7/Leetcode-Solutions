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

    # TC:- (2N) 2 PASS
    #SC:- O(1)
    # def removeNthFromEnd(self,head,n):
    #     p=head
    #     countOfNodes=0
    #     while p:
    #         p=p.next
    #         countOfNodes+=1
        
    #     if n==countOfNodes:
    #         head=head.next
    #         return head

    #     idx= countOfNodes - n
    #     i=0
    #     curr=head
    #     while i<idx-1:
    #         curr=curr.next
    #         i+=1
    #     curr.next=curr.next.next
    #     return head


    #TC: O(N)
    #SC:- O(1)
    
    def removeNthFromEnd(self,head,n):
        p=head
        q=head
        i=0
        while i<n:
            q=q.next
            i+=1
        
        prev=dummyNode=ListNode(-1)
        dummyNode.next= head
        while q:
            prev=p
            p=p.next
            q=q.next
        
        
        prev.next=prev.next.next
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
head=s1.take_input()
new_head = s1.removeNthFromEnd(head,6)
s1.printLL(new_head)



