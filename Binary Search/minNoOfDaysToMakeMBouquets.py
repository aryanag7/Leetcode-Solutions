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
#     O(MAX(ARRAY) * N)
#     SC:- O(1)

    def minDays(self, bloomDay, m, k):
        n=len(bloomDay)
        if m * k > n:
            return -1
        
        max_wait = max(bloomDay)

        for i in range(1,max_wait+1):
            #check if waiting for this i days helps us to make m bouquets
            bouquets_made = 0 
            flowers_used = 0

            for flower in bloomDay:
                if i >= flower:
                    flowers_used+=1
                    if flowers_used == k:
                        bouquets_made+=1
                        flowers_used =0
                else:
                    flowers_used =0
            
            if bouquets_made >= m:
                return i
            


            
    def isPossible(self,wait_days,bloomDay,m,k):
        bouquets_made = 0 
        flowers_used = 0

        for flower in bloomDay:
            if wait_days >= flower:
                flowers_used+=1
                if flowers_used == k:
                    bouquets_made+=1
                    flowers_used =0
            else:
                flowers_used =0
        
        if bouquets_made >= m:
            return True
        return False
    

    # TC:- O(LOG(MAX(ARRAY)) * N)
    # SC:- O(1)
    def minDays(self, bloomDay, m, k):
        n=len(bloomDay)
        if m * k > n:
            return -1
        
        max_wait = max(bloomDay)

        low=1
        high = max_wait
        ans=-1

        while low<=high:
            mid = low+(high-low)//2

            if self.isPossible(mid,bloomDay,m,k):
                ans= mid
                high = mid-1
            
            else:
                low = mid+1
        
        return ans  # or low 


                
    
s1 = Solution()
bloomDay =  [1,10,3,10,2]
m = 3
k = 1
print(s1.minDays(bloomDay,m,k))

    




