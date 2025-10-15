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
    # TC:- O(N * log(N))
    # sc:- O(N)
    def lastStoneWeight(self, stones):
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, -s)

        while len(maxHeap)>1:
            s1=  -heapq.heappop(maxHeap)
            s2 = -heapq.heappop(maxHeap)

            if s1!=s2:
                heapq.heappush(maxHeap,-abs(s1-s2))
        
        return -maxHeap[0]

  


s1= Solution()
stones = [2,7,4,1,8,1]
print(s1.lastStoneWeight(stones))



