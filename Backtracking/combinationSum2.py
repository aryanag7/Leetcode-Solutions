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

   
    def combinationSum2(self, candidates, target):
        
        # Uses extra space to convert from set to list to return the answer
        # def combinationSum2(candidates,target,ind,ds):
        #     if ind==len(candidates):
        #         if target==0:
        #             uniqueCombinations.add(tuple(ds))
        #         return 
            


        #     if target>=candidates[ind]:
        #         combinationSum2(candidates,target-candidates[ind],ind+1,ds+[candidates[ind]])
            
        #     combinationSum2(candidates, target, ind+1,ds)


        # uniqueCombinations = set()
        # candidates.sort()

        # combinationSum2(candidates,target,0,[])

        # ans = [ list(t) for t in uniqueCombinations ]

        # return ans
    
            
        

        # TC:- O(2^n)
        # SC:- O(N) stack space, O(n * 2^n) for ans
        ans=[]
        candidates.sort()

        def combinationSum2Helper(candidates,target,ind,ds):
            if target==0:
                ans.append(ds)
                return
                
            if ind==len(candidates):
                if target==0:
                    ans.append(ds)    
                return 

            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                
                # recursion only happens here thats why you need to add combinations with target 0 before reaching the end as it might not reach the end always.
                if target>=candidates[i]:
                    combinationSum2Helper(candidates,target-candidates[i],i+1,ds+[candidates[i]])
                

        
        combinationSum2Helper(candidates,target,0,[])
        return ans





     
    


s1 = Solution()
candidates =[2,5,2,1,2]
target = 5
print(s1.combinationSum2(candidates,target))

    


