import bisect
import sys
import os
import math
from collections import defaultdict
from collections import Counter
from typing import Deque
from collections import deque
from itertools import accumulate, count
import heapq

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
    
    # TC:- O(NlogN) - N is total nodes of all lists pushed into minheap and popped out N times       N = k * N - k lists each of size N assuming
    # SC:- O(k*N) + O(K*N)
    #better than pairwise merge using merge 2 lists TC : O(K*k*N)
    def mergeKLists(self, lists):
        if len(lists)==0:
            return None

        minHeap = []
        for list in lists:
            head= list
            while head:
                heapq.heappush(minHeap, (head.val))
                head = head.next
        
        dummyNode = ListNode(-1)
        prev  = dummyNode
        while len(minHeap)>0:
            nodeVal = heapq.heappop(minHeap)
            node = ListNode(nodeVal)
            prev.next = node
            prev=prev.next
        
        return dummyNode.next
    



    # TC:- O(KlogK + k*N log K) - N is size of each list and K is number of lists
    # SC:- O(k*N) + O(K*N)
    def mergeKLists(self, lists):
        if len(lists)==0:
            return None
        
        tie = count()  
        
        minHeap = []
        for li in lists:
            heapq.heappush(minHeap, (li.val,next(tie),li))
        
        prev = dummy = ListNode(-1)

    # K*N log K - as you would be ultimately pushing all nodes into heap
        while len(minHeap) >0:
            val, node = heapq.heappop(minHeap)

            prev.next = node
            prev=prev.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val,next(tie),node.next))
        
        return dummy.next

                
        
   



        
            
s1= Solution()
arr = [1,2,3,4,5]
k = 4
x = 3
print(s1.findClosestElements(arr,k,x))



