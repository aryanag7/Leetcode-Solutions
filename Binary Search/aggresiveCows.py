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


class Solution:
    # TC:- NLOGN + ((MAX - MIN) * N )
    # SC:- O(1)
    def aggressiveCows(self, stalls, k):
        n=len(stalls)

        stalls.sort()

        ans = -1
        for min_dist in range(1, max(stalls)-min(stalls)+1):
            cows_placed = 1
            last_placed = 0
            for i in range(1,n):
                if stalls[i]-stalls[last_placed] >= min_dist:
                    last_placed = i
                    cows_placed+=1

            
            if cows_placed >= k:
                ans = min_dist
        
        return ans

    def isPossible(self,min_distance, stalls, k):
        n=len(stalls)
        cows_placed = 1
        last_placed = 0
        for i in range(1,n):
            if stalls[i]-stalls[last_placed] >= min_distance:
                last_placed = i
                cows_placed+=1

        
        return cows_placed >= k
      

    # TC:- NLOGN + (LOG(MAX - MIN+1) * N )
    # SC:- O(1)
    def aggressiveCows(self, stalls, k):
        n=len(stalls)
        stalls.sort()
        low=1 #or can be min of all consecutive elements if placing n cows
        high = max(stalls)-min(stalls)
        ans= -1

        while low<=high:
            mid  = low + (high-low)//2

            if self.isPossible(mid, stalls, k):
                ans= mid
                low = mid+1

            else:
                high = mid-1
        
        return ans #or high







        

            
s1 = Solution()
stalls =[0,3,4,7,10,9]
k = 4
print(s1.aggressiveCows(stalls,k))

    




