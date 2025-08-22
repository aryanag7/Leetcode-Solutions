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
    # TC:- O(MAX(NUMS)* N)
    # SC:- O(1)
    def smallestDivisor(self, nums, threshold):
        n=len(nums)
        max_divisor = max(nums)

        for divisor in range(1,max_divisor+1):
            s=0
            for num in nums:
                s+= math.ceil(num/divisor)
            
            if s<=threshold:
                return divisor
            
    def isPossible(self,divisor,nums,threshold):
        s=0
        for num in nums:
            s+= math.ceil(num/divisor)
        
        return s<= threshold
        

    
    # TC:- O(LOG(MAX(NUMS))* N)
    # SC:- O(1)
    def smallestDivisor(self, nums, threshold):
        n=len(nums)
        max_divisor = max(nums)

        low = 1
        high = max_divisor
        ans=-1

        while low<=high:
            mid = low + (high-low)//2

            if self.isPossible(mid,nums,threshold):
                ans=mid
                high = mid-1
            else:
                low = mid+1
        return ans



    

    





                
    
s1 = Solution()
nums = [44,22,33,11,1]
threshold = 5
print(s1.smallestDivisor(nums,threshold))

    




