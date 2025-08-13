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
    # TC:- O( N * N)
    # SC:- O(K+1)
    def subarraysWithKDistinct(self, nums, k):
        ans=0
        n=len(nums)

        for i in range(0,n):
            distinctCount = set()
            for j in range(i,n):
                distinctCount.add(nums[j])
                
                if len(distinctCount)>k:
                    break
                elif len(distinctCount)==k:
                    ans +=1
        
        return ans
    



    def numOfGoodSubarrays(self,nums,k):
        if k<0:
            return 0
        l=0
        r=0
        ans=0
        n=len(nums)

        d=defaultdict(int)

        while r<n:
            d[nums[r]]+=1


            while len(d)>k:
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    d.pop(nums[l])
                l+=1

            ans += (r-l+1)
            r+=1
        
        return ans
    

    # TC:- O 2 *( N + N)
    # SC:- O(K+1)
    def subarraysWithKDistinct(self, nums, k):
        totalSubarrys = self.numOfGoodSubarrays(nums,k) # with odds=k and odds<k

        lessThanKSubarrays = self.numOfGoodSubarrays(nums,k-1) #odds < k means <=k-1

        return totalSubarrys - lessThanKSubarrays

    





        

s1 = Solution()
nums = [1,2,1,2,3]
k = 2
print(s1.subarraysWithKDistinct(nums,k))

    


