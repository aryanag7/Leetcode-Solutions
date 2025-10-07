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
    # TC:- O(N) + NlogN
    # SC:- O(N)
    def topKFrequent(self, nums, k):
        d = defaultdict(int)
        for num in nums:
            d[num]+=1
        
        sorted_d = sorted(d.items(), key= lambda x:x[1], reverse= True)
        
        ans=[]
        for index, (key,freq) in enumerate(sorted_d):
            ans.append(key)

            if index == k-1:
                break

        
        return ans
    

    # TC:- O(N) + NlogK
    # SC:- O(N) + O(K)
    def topKFrequent(self, nums, k):
        d = defaultdict(int)
        for num in nums:
            d[num]+=1

        items = [(key,val) for key,val in d.items()]
        minHeap = []
        for i in range(0,k):
            val,freq = items[i][0], items[i][1]
            heapq.heappush(minHeap,(freq,val))
        
        for i in range(k,len(items)):
            val,freq = items[i][0], items[i][1]
            if freq > minHeap[0][0]:
                heapq.heapreplace(minHeap, (freq,val))
        
        return [ key for val,key in minHeap]
    

        #in single pass
        # d = defaultdict(int)
        # for num in nums:
        #     d[num]+=1

        # minHeap = []
        # for key,freq in d.items():
        #     if len(minHeap)<k:
        #         heapq.heappush(minHeap,(freq,key))
        #     elif freq > minHeap[0][0]:
        #         heapq.heapreplace(minHeap, (freq,key))
        
        # return [ key for val,key in minHeap]


s1= Solution()
nums = [1,1,1,2,2,3]
k = 2
print(s1.topKFrequent(nums,2))



