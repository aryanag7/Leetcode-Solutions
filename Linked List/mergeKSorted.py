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


    # TC:- O(N* LOGN) - N is total number of nodes in all linked lists, N lists each of size k so O( N*K) 
    # SC:- O( N*K)  + O( N*K)  for new linkedlist
    # def mergeKLists(self, lists):
    #     temp=[]
        
    #     for li in lists:
    #         p=li
    #         while p:
    #             temp.append(p.val)
    #             p=p.next
        
    #     temp.sort()

    #     curr=dummyNode= ListNode(-1) 

    #     for ele in temp:
    #         node= ListNode(ele)
    #         curr.next=node
    #         curr=curr.next
        
    #     return dummyNode.next

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

    """
    First two lists: N + N = 2N

    Then result with third: 2N + N = 3N

    Then with fourth: 3N + N = 4N


    Up to the K-th list: KN

    The total work becomes: N(1+2+3+...+K)= ( N *  K(K+1)/2 ~ O(N⋅K ^2 )
    
    """


    # SC:- O(1) 
    def mergeKLists(self, lists):
        if len(lists)==0:
            return None
        
        head=lists[0]


        # Assume:- N different lists, each of size K
        for i in range(1,len(lists)):

            # N1+N2
            head= self.mergeTwoLists(head,lists[i])
        
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
new_head = s1.reverseKGroup(head,3)
s1.printLL(new_head)



