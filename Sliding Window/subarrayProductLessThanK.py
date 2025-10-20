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
    # TC:- O(N*N)
    # SC:- O(1)
    def numSubarrayProductLessThanK(self, nums,k):
        n = len(nums)
        count = 0

        for i in range(0,n):
            s = 1
            for j in range(i,n):
                s*= nums[j]

                if s<k:
                    count+=1

                elif s>=k:
                    break
        return count
    


    # TC:- O(N + N) - at max n removals from left, sometimes 2 removal, sometimes 4
    # SC:- O(1)
    def numSubarrayProductLessThanK(self, nums,k):
        n = len(nums)
        count = 0

        product = 1
        left = 0
        right = 0

        while right<n:
            product*= nums[right]

            while product>=k and left<=right:
                product = product // nums[left]
                left+=1
           
            if product < k:
                count+= (right-left+1)
            right+=1

        return count 








s1 = Solution()
nums = [57,44,92,28,66,60,37,33,52,38,29,76,8,75,22]
k = 18
print(s1.numSubarrayProductLessThanK(nums,k))

    


