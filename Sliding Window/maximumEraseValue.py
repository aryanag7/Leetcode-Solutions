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
    # SC:- O(N)
    # def maximumUniqueSubarray(self, nums):
    #     n=len(nums)
    #     ans = 0

    #     for i in range(0,n):
    #         s=0
    #         seen = set()
    #         for j in range(i,n):
    #             s+= nums[j]

    #             if nums[j] in seen:
    #                 s-=nums[j]
    #                 break

    #             seen.add(nums[j])


    #         ans = max(ans, s)
        
    #     return ans
    

    # TC:- O(N+N)
    # SC:- O(N)
    def maximumUniqueSubarray(self, nums):
        n=len(nums)

        l = 0
        r = 0
        d = defaultdict(int)
        s= 0
        ans = 0

        while r<n:
            s += nums[r]
            d[nums[r]]+=1

            while r-l+1 > len(d):
                d[nums[l]]-=1
                s-= nums[l]
                if d[nums[l]]==0:
                    d.pop(nums[l])
                l+=1


            ans = max(ans, s)
            r+=1

        return ans





s1 = Solution()
nums =[5,2,1,2,5,2,1,2,5]
print(s1.maximumUniqueSubarray(nums))

    


