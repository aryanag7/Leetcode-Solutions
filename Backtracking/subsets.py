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
    def subsets(self, nums):

        #TC:- O(2^N)
        #SC:- O(N) stack space, 0(n * 2^n) if considering ans array (each subset of size n)
        def subsetHelper(nums,index,ds):
            if index==len(nums):
                ans.append(ds)
                return 

            subsetHelper(nums,index+1,ds+[nums[index]])

            subsetHelper(nums,index+1,ds)

        ans=[]
        subsetHelper(nums,0,ds=[])

        return ans


s1 = Solution()
nums = list(map(int, input().split()))
print(s1.subsets(nums))

    


