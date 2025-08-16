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
    # SC:- O(1) if excluded ans array
    def nextGreaterElements(self, nums):
        n=len(nums)
        ans=[-1]*n

        for i in range(0,n):
            
            for j in range(i+1, i+n):
                new_ind = j%n
                if nums[new_ind]> nums[i]:
                    ans[i] = nums[new_ind]
                    break

        return ans

            
            

    # TC:- O(2N + 2N)
    # SC:- O(2N) if excluded ans array
    # def nextGreaterElements(self, nums):
    #     n=len(nums)
    #     ans=[-1]*n
    #     stack=[nums[-1]]

    #     for i in range(2*n-2,-1,-1):
    #         new_ind = i%n

    #         while stack and nums[new_ind]>=stack[-1]:
    #             stack.pop()
            
    #         if stack and i<n:
    #             ans[i] = stack[-1]
            
            

    #         stack.append(nums[new_ind])
        
    #     return ans




  
 


s1 = Solution()
nums = [1,2,1]
print(s1.nextGreaterElements(nums))

    


