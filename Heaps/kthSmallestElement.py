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

    # TC:- O(NlogN)
    # SC:- O(1)
    def findKthSmallest(self, nums, k):
        nums.sort()
        return nums[k-1]
    
    # TC :- O(NlogK) - heap size is O(K)
    # SC :- O(K)
    def findKthSmallest(self, nums, k):
        n=len(nums)

        maxHeap = []

        for i in range(0,k):
            heapq.heappush(maxHeap, -nums[i])

        for i in range(k,n):
            if nums[i] < -maxHeap[0]:
                heapq.heapreplace(maxHeap, -nums[i])
        
        return -maxHeap[0]
        

s1= Solution()
nums = [7,10,4,3,20,15]
print(s1.findKthSmallest(nums,3))



