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

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        n=len(nums)
        self.k = k

        self.minHeap = []
        for i in range(0,k):
            if i<len(nums):
                heapq.heappush(self.minHeap, nums[i])
        
        for i in range(k,n):
            if i<len(nums) and nums[i] > self.minHeap[0]:
                heapq.heapreplace(self.minHeap, nums[i])
        

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)

        elif val>self.minHeap[0]:
            heapq.heapreplace(self.minHeap, val)

        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)