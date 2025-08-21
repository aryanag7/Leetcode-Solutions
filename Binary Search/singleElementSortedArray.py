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
    # SCL:- O(1)
    # def singleNonDuplicate(self, nums) -> int:
    #     n=len(nums)
    #     if n==1:
    #         return nums[0]

    #     for i in range(0,n):
    #         if i==0 and nums[i] != nums[i+1]:
    #             return nums[0] 
            
    #         elif i==n-1 and nums[i] != nums[i-1]:
    #             return nums[n-1]
            
    #         else:
    #             if nums[i]!= nums[i+1] and nums[i]!=nums[i-1]:
    #      
    #            return nums[i]



    # TC:- O(LOGN)
    # SC:- O(1)
    def singleNonDuplicate(self, nums):
        n=len(nums)
        if n==1:
            return nums[0]
        
        if nums[0]!=nums[1]:
            return nums[0]
        
        if nums[-1]!=nums[-2]:
            return nums[-1]

        low=1
        high=n-2
        while low<=high:
            mid  = low + (high-low)//2

            if nums[mid]!= nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]

            #even index - check if its even odd or odd even
            if mid%2==0:
                #even odd
                if nums[mid]==nums[mid+1]:
                    low = mid+1
                
                #odd even
                else:
                    high = mid-1

            #odd index - check if its odd even or even odd
            else:
                # even odd
                if nums[mid]==nums[mid-1]:
                    low = mid+1
                # odd even
                else:
                    high = mid-1


            #optimized conditions

            if mid%2==0 and nums[mid]==nums[mid+1] or mid%2==1 and nums[mid]==nums[mid-1]:
                low=mid+1
            
            else:
                high = mid-1



        
            

    
s1 = Solution()
nums = [1,1,2,3,3,4,4,8,8]
print(s1.singleNonDuplicate(nums))

    


