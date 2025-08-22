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
    # TC:- O(MAX(PILES) * N)
    # SC:- O(1)
    def minEatingSpeed(self, piles, h):
        max_speed = max(piles)

        for speed in range(1,max_speed+1):
            hrs_taken = 0
            for pile in piles:
                if speed>pile:
                    hrs_taken+=1
                
                else:
                    hrs_taken+= (math.ceil(pile/speed))
            
            if hrs_taken<= h:
                return speed
            
    def isPossible(self,speed, piles, h):
        hrs_taken = 0
        for pile in piles:
            if speed>pile:
                hrs_taken+=1
            else:
                hrs_taken+= (math.ceil(pile/speed))
        
        return hrs_taken<=h
        


    #TC:- O(LOG(MAX SPEED) * N)
    # SC:- O(1) - Optimized the searching of speed, rather thab linear search we do binary search 
    def minEatingSpeed(self, piles, h):
        max_speed = max(piles)
        low=1
        high = max_speed
        ans= high

        while low <=high:
            #Mid speed

            mid = low + (high-low)//2
            #good speed less hrs but need to find least speed
            if self.isPossible(mid, piles, h):
                ans = mid
                high = mid-1
            else:
                #small speed - more hrs
                low = mid+1
        
        return ans


        
    
s1 = Solution()
piles = [30,11,23,4,20]
h = 6
print(s1.minEatingSpeed(piles,h))

    




