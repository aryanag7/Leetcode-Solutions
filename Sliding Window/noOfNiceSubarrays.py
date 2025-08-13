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
    # SC:- O(1)
    # def numberOfSubarrays(self, nums,k):
    #     ans=0
    #     n=len(nums)

    #     for i in range(0,n):
    #         odds=0
    #         for j in range(i,n):
    #             if nums[j]%2==1:
    #                 odds+=1
                
    #             if odds==k:
    #                 ans+=1
        
    #     return ans
    
    def numOfGoodSubarrays(self, nums, k):  
        if k<0:
            return 0
        ans=0
        l=0
        r=0
        n=len(nums)
        odds=0

        while r<n:
            if nums[r]%2==1:
                odds+=1

            while odds>k:
                if nums[l]%2==1:
                    odds-=1
                l+=1

            ans+= (r-l+1)
            r+=1
        
        return ans
     
    def numberOfSubarrays(self, nums, k):
        totalSubarrys = self.numOfGoodSubarrays(nums,k) # with odds=k and odds<k

        lessThanKSubarrays = self.numOfGoodSubarrays(nums,k-1) #odds < k means <=k-1

        return totalSubarrys - lessThanKSubarrays







        

s1 = Solution()
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(s1.numberOfSubarrays(nums,k))

    


