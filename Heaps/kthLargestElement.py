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
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        n=len(nums)
        return nums[k-1]
    

    # TC :- O(NlogK) - heap size is O(K)
    # SC :- O(K)
    def findKthLargest(self, nums, k):
        n=len(nums)

        minHeap = []

        for i in range(0,k):
            heapq.heappush(minHeap, nums[i])

        for i in range(k,n):
            if nums[i] > minHeap[0]:
                heapq.heapreplace(minHeap, nums[i])
        
        return minHeap[0]
        




s1= Solution()
nums = [3,2,1,5,6,4]
print(s1.findKthLargest(nums,2))



