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
    def nextGreaterElement(self, nums):
        n=len(nums)
        ans= [-1]*n

        for i in range(0,n):
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    ans[i] = nums[j]
                    break

        
        return ans
    

    # TC:- O(N+N) similar to sliding window you may remove 3 ele, then 3 then 4 at most N
    # SC:- O(N)
    # it’s a monotonic decreasing stack because we pop smaller elements so the stack always holds strictly greater candidates for next greater element.
    
    def nextGreaterElement(self, nums):
        n=len(nums)
        ans= [-1]*n

        stack=[nums[-1]]

        for i in range(n-2,-1,-1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1]
        

            stack.append(nums[i])
        
        return ans





  
 


s1 = Solution()
nums = [1,3,0,0,1,2,4]
print(s1.nextGreaterElement(nums))

    


