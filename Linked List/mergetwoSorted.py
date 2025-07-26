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
    # TC:- O(N) Ultimately
    # SC:- O(LEN(L1) + LEN(L2))
    # def mergeTwoLists(self, list1, list2):
    #     if list1 is None:
    #         return list2
    #     if list2 is None:
    #         return list1
        
    #     dummyNode=ListNode(-1)
    #     curr=dummyNode

    #     while list1 and list2:
    #         if list1.val<=list2.val:
    #             newNode= ListNode(list1.val)
    #             curr.next=newNode
    #             list1=list1.next
    #         else:
    #             newNode= ListNode(list2.val)
    #             curr.next=newNode
    #             list2=list2.next
            
    
    #         curr=curr.next
        
    #     while list1:
    #         newNode= ListNode(list1.val)
    #         curr.next=newNode
    #         curr=curr.next
    #         list1=list1.next
        
    #     while list2:
    #         newNode= ListNode(list2.val)
    #         curr.next=newNode
    #         curr=curr.next
    #         list2=list2.next
        
    #     return dummyNode.next

    

    # TC:- O(N)
    # SC:- O(1) No new nodes creation, just link changes
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        dummyNode= ListNode(-1)
        prev=dummyNode

        while list1 and list2:
            if list1.val<=list2.val:
                prev.next= list1
                list1=list1.next
            
            else:
                prev.next=list2
                list2=list2.next
            
            prev=prev.next
        
        if list1:
            prev.next=list1

        if list2:
            prev.next=list2
        
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
new_head = s1.mergeTwoLists(head1,head2)
s1.printLL(new_head)



