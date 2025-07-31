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
    # For each subset, you're doing ds + [nums[i]], which creates a copy of the current list — this takes O(n) time for a list of size up to n.
    # At most, ds can grow to size n (if you include all elements).
    #TC:- O(2^n * n) 
    #SC:- O(N) stack space and for ans O(2^n * k)
    def subsetsWithDup(self, nums):

        nums.sort()

        def subsetsWithDupHelper(nums,ind,ds):
            ans.append(ds)

            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]:
                    continue

                subsetsWithDupHelper(nums,i+1,ds+[nums[i]])

        ans=[]
        subsetsWithDupHelper(nums,0,[])
        return ans








s1 = Solution()
nums = [1,2,2]
print(s1.subsetsWithDup(nums))

    


