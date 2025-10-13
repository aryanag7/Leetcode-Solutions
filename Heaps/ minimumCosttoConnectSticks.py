import bisect
import sys
import os
import math
from collections import defaultdict
from collections import Counter
from typing import Deque
from collections import deque
from itertools import accumulate
import heapq

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Redirect stdin and stdout
sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')



class Solution:
    # TC:- O(N-1) * N
    # SC:- O(1)
    def connectSticks(self, sticks):
        cost = 0

        n=len(sticks)
        while n-1>0:
            
            s1= min(sticks)
            sticks.remove(s1)

            s2 = min(sticks)
            sticks.remove(s2)

            cost+= (s1+s2)

            sticks.append(s1+s2)

            n-=1

        return cost
    

    # TC:- O(N-1 * logN) - min from heap is log(heap size)
    # SC:- O(N) 
    def connectSticks(self, sticks):
        minHeap = list(sticks)
        heapq.heapify(minHeap)

        cost = 0 
        n=len(minHeap)
        while len(minHeap)>1:
            
            s1 = heapq.heappop(minHeap)
            
            s2 = heapq.heappop(minHeap)

            cost+= (s1+s2)

            minHeap.append(s1+s2)

            n-=1

        return cost



  


s1= Solution()
sticks  = [1,8,3,5]
print(s1.connectSticks(sticks))



