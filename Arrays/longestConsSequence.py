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
    # TC:- (NLOGN)
    # SC:- O(n) sorting using tim sort
    # def longestConsecutive(self, nums):
    #     if not nums:
    #         return  0

    #     ans=1
    #     nums.sort()

    #     n=len(nums)
    #     currLen=1
    #     for i in range(1,n):
    #         if nums[i]==nums[i-1]+1:
    #             currLen+=1
    #         elif nums[i] == nums[i-1]:
    #             continue
    #         else:
    #             currLen=1
            
    #         ans=max(ans,currLen)

    #     return ans
    

    # TC:- near about O(N) if iterated on set rather than nums check with [1,2,3,4] -> you iterate from 1 until 4 inside while but dont iterate for 2,3,4 , its jsut iterated once
    # SC:- O(1)
    def longestConsecutive(self, nums):

        seen= set(nums)
        ans=0

        for num in nums:
            if num-1 not in seen:
                count=1
                while num+1 in seen:
                    count+=1
                    num = num+1

                ans=max(ans,count)
            
        return ans


s1 = Solution()
nums =  [1,0,1,2]
print(s1.longestConsecutive(nums))
    

