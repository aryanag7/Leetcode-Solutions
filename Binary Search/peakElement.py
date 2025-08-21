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
    # TC:- O(N)
    # SC:- O(1)
    def findPeakElement(self, nums):
        if len(nums)==1:
            return 0
        
        if nums[0]>nums[1]:
            return 0
        
        if nums[-1]>nums[-2]:
            return len(nums)-1
        
        n=len(nums)
        for i in range(1,n-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
            
    
    # TC:- O(LOGN)
    # SC:- O(1)

    # Idea is to solve for 1 peak and for multiple peaks just trim down the search space to reduce the problem to 1 peak mountain from multiple peak mountains
    def findPeakElement(self, nums):
        n=len(nums)
        if n==1:
            return 0
        
        if nums[0]>nums[1]:
            return 0
        
        if nums[-1]>nums[-2]:
            return n-1
        
        low=1
        high =n-2

        while low<=high:
            mid = low + (high-low)//2

            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            
            elif nums[mid]>nums[mid-1]:
                low = mid+1
            
            else:
                #considers the case for both mid > mid + 1 increasing from right to left and when mid is smaller than both side so can go anywhere doesnt matter
                high = mid-1
        


    


    



    
s1 = Solution()
nums = [1,2,1,2,1]
print(s1.findPeakElement(nums))

    


