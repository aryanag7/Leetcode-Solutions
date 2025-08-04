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
    # TC:- O(N^2)
    # SC:- O(1)
    # def twoSum(self, nums, target):
    #     for i in range(0,len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i]+nums[j]==target:
    #                 return [i,j]
        
    #     return -1


    # TC:- O(N)
    # SC:- O(N)
    def twoSum(self, nums, target):
        d = {}

        for idx,num in enumerate(nums):
            secondNum = target- num
            if secondNum in d:
                return [idx,d[secondNum]]
            
            d[num]= idx
        return -1

   


s1 = Solution()
nums =[-3,4,3,90]
target = 0
print(s1.twoSum(nums,target))

    


