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
    # TC:- O(LOGN)
    # SC:- O(1)
    def search(self, nums, target):
        n=len(nums)
        low=0
        high =n-1
        ans=-1

        while low<=high:
            mid = low + (high-low)//2

            if nums[mid]==target:
                ans=mid
                return ans
            
            #left half sorted
            elif nums[low]<=nums[mid]:
                if target>=nums[low] and target<=nums[mid]:
                    high= mid
                else:
                    low = mid +1
        
            else:
                #right half sorted
                if target>= nums[mid] and target<=nums[high]:
                    low=mid
                else:
                    high = mid-1

            #left half sorted
         
            
        return ans


    
s1 = Solution()
nums = [1,3]
target = 2
print(s1.search(nums,target))

    


