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
    # TC:- O(N * N)
    # SC:- O(1)
    def numSubarraysWithSum(self, nums, goal):
        ans=0
        n=len(nums)

        for i in range(0,n):
            s=0
            for j in range(i,n):
                s+=nums[j]

                if s>goal:
                    break

                elif s==goal:
                    ans+=1
        
        return ans
    
    # cannot directly apply sliding window as once you find an invalid window, you shrink from the left and once its valid you move r but there could be more subarrays between the shrinked valid window which you will miss out

    # count subarrays ending at r with variable l (bw window l - r)
    # ex: 1 0 0 1 ->   1 0 0 1,   0 0 1,   0 1,   1 ending fixed at 1

    # count subarrays with sum<=k means with sum =k and sum<k which is total count lets say
    # now we need need to subtract the sum<k part which is sum <= (k-1)

    # TC:- O ( 2 * (N + N))
    # SC:- O(1) 
    def numSubarrays(self, nums, goal):  
        if goal-1 <0:
            return 0
        ans=0
        l=0
        r=0
        n=len(nums)
        s=0

        while r<n:
            s+= nums[r]

            while s>goal:
                s-= nums[l]
                l+=1

            ans+= (r-l+1)
            r+=1
        
        return ans
    def numSubarraysWithSum(self, nums, goal):
        totalSubarrys = self.numSubarrays(nums,goal) # with sum=k and sum<k

        lessThanKSubarrays = self.numSubarrays(nums,goal-1)

        return totalSubarrys - lessThanKSubarrays


        

s1 = Solution()
nums = [1,2,1]
goal = 3
print(s1.numSubarraysWithSum(nums,goal))

    


