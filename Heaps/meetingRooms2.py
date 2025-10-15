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
    # TC:- O(N logN)
    # SC:- O(1)
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x:x[0])
        minHeap = []

        # rooms = 0
        n=len(intervals)
        for i in range(0,n):
            s,e = intervals[i]

            #re use this room stored in heap 
            if minHeap and s >= minHeap[0][0]:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap,(e,s))
            
        
        return len(minHeap)

  


s1= Solution()
intervals =[[5,8],[6,8]]
print(s1.minMeetingRooms(intervals))



