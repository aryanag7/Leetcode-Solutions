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
    def combinationSum(self, candidates, target):
        
        #TC:- O(2^N)
        #SC:- O(N) stack space, O(N * 2^n) for ans array considering each subset of size n, 

        # add new base case to handle target==0 if it has negative numbers
        def combinationSumHelper(candidates,target,ind,ds):
            if ind==len(candidates):
                if target==0:
                    ans.append(ds)
                return 


            if  target>=candidates[ind]:
                combinationSumHelper(candidates,target-candidates[ind], ind, ds+[candidates[ind]])


            combinationSumHelper(candidates, target,  ind+1, ds)

        ans=[]
        combinationSumHelper(candidates,target,0,[])
        
        return ans
        
    


s1 = Solution()
candidates = [2,3,6,7]
target = 7
print(s1.combinationSum(candidates,target))

    


