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
    def findMin(self, nums):
        n=len(nums)
        low=0
        high = n-1
        ans= float('inf')

        while low<=high:
            mid = low + (high-low)//2

            if nums[low]==nums[mid]==nums[high]:
                ans = min(ans, nums[low])
                low+=1
                high-=1
            
            elif nums[mid]>=nums[low]:
                ans = min(ans, nums[low])
                low = mid+1
            
            else:
                ans= min(ans,nums[mid])
                high = mid-1
        
        return ans
        

   

    
s1 = Solution()
nums = [2,2,2,0,1]
print(s1.findMin(nums))

    


