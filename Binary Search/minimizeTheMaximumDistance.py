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
    # TC:- O(K * N) + N
    # def minmaxGasDist(self, stations,  k):
    #     n=len(stations)
    #     placed = [0]* (n-1)
    #     for k in range(1,k+1):
    #         maxi = -1
    #         max_index = -1

    #         for i in range(0,n-1):
    #             diff = stations[i+1] - stations[i]
    #             div_len = diff/ (placed[i]+1)

    #             if div_len > maxi:
    #                 maxi = div_len
    #                 max_index = i
            
    #         placed[max_index]+=1
        
    #     ans = -1
    #     for i in range(0,n-1):
    #         diff = stations[i+1] - stations[i]
    #         div_len = diff/ (placed[i]+1)

    #         ans = max(ans, div_len)
        
    #     return ans
    

    def isPossible(self,max_distance, stations, k):
        n=len(stations)
        placed =0

        for i in range(0,n-1):
            diff = stations[i+1]-stations[i]
            if diff % max_distance ==0:
                placed+=  (diff // max_distance)-1
            else:
                placed+=  (diff // max_distance)

        return placed <=k


    # TC:- O(N) + O(LOG(RANGE))* N) 

    def minmaxGasDist(self, stations,  k):
        low = 0
        high = 0
        n=len(stations)

        for i in range(0,n-1):
            high = max(high,stations[i+1]-stations[i])
        
        while high - low > 10**-6:
            mid = low + (high-low)/2

            if self.isPossible(mid, stations, k):
                ans = mid
                high = mid
            else:
                low = mid
        
        return ans






s1 = Solution()
arr = [1,13, 17, 23]
k = 5
print(s1.minmaxGasDist(arr,k))

    




