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
    # TC:- O(SUM(ARR) - max(arr) +1 * N)
    # SC:- O(1)
    def shipWithinDays(self, weights, days):
        min_weight = max(weights)
        max_weight = 0

        for i in weights:
            max_weight+=i

        for capacity in range(min_weight, max_weight+1):
            #check if can ship all packages within d days
            days_taken = 1
            s=0
            shippedAll = True
            for num in weights:
                if num > capacity:
                    shippedAll = False
                    break

                s+= num

                if s> capacity:
                    days_taken+=1
                    s= num
            
            if shippedAll and  days_taken <= days:
                return capacity
            
    
    def isPossible(self,capacity, weights, days):
        days_taken = 1
        s=0
        for num in weights:
            s+= num

            if s> capacity:
                days_taken+=1
                s= num
        
        return days_taken <= days        

            
        

    # TC:- O(log(SUM(ARR -max(arr)+1) * N)
    # SC:- O(1)
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = 0
        for i in weights:
            high+=i
        
        ans = high

        while low <= high:
            mid = low + (high-low)//2

            if self.isPossible(mid, weights, days):
                ans = mid
                high = mid-1
            else:
                low =  mid+1
        
        return ans
        
                
            
s1 = Solution()
weights = [1,2,3,1,1]
days = 4
print(s1.shipWithinDays(weights,days))

    




