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
    # TC:- O(N) + O(NlogN) + O(KlogK)
    # SC:- O(N) + O(K)
    def findClosestElements(self, arr, k, x):
        d = []
        for ele in arr:
            d.append((ele,abs(ele-x)))
        
        ans =  [num for num,close in sorted(d, key= lambda x:(x[1],x[0]))[:k]]

        ans.sort()

        return ans
    


    # TC:- O(N) + O(KlogN) + (KlogK)  ------ but if k ~ n then NlogN
    # SC:- O(N) + O(K)
    def findClosestElements(self, arr, k, x):
        minHeap = []
        for ele in arr:
            minHeap.append((abs(ele-x),ele))

        heapq.heapify(minHeap)

        ans=[]
        for i in range(0,k):
            _,num = heapq.heappop(minHeap)
            ans.append(num)
        
        ans.sort()

        return ans
    


    # TC:- O(N) + O(NlogK) - optimized over above where we just maintain heap size of K, ---------WORST CANDIDATE ROOT-------- here is max freq and max word as we need lest freq and least word
    # SC:- O(N) + O(K)
    def findClosestElements(self, arr, k, x):
        pairs = []
        for ele in arr:
            pairs.append((abs(ele-x),ele))
        
        maxHeap = []
        n=len(pairs)
        for close,num in pairs:
            heapq.heappush(maxHeap, (-close,-num))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        print(maxHeap)
        return sorted( -num for _,num in maxHeap)
            
s1= Solution()
arr = [1,2,3,4,5]
k = 4
x = 3
print(s1.findClosestElements(arr,k,x))



