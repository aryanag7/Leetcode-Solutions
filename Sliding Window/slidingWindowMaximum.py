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
    # TC:- O(N * K)
    # SC:- O(1)
    # def maxSlidingWindow(self, nums, k):
    #     ans=[]
    #     n=len(nums)

    #     for i in range(0,n-k+1):
    #         maxi=float('-inf')
    #         for j in range(i,i+k):
    #             maxi= max(maxi, nums[j])
            
    #         ans.append(maxi)

    #     return ans
    

    def maxSlidingWindow(self, nums, k):
        n=len(nums)
        maxi = float('-inf')

        for i in range(k):
            maxi = max (maxi, nums[i])

        ans=[maxi]
        l=0
        r=k

        while r<n:
            maxi = max(maxi, nums[r])
            r+=1

            if nums[l] == maxi:
                new_maxi = float('-inf')
                for i in range(l+1,r):
                    new_maxi = max( new_maxi, nums[i])
                maxi = new_maxi
            l+=1

            ans.append(maxi)
        

        return ans
    

    # TC:- O(N) 
    # SC:- O(K) if array is strictly decreasing
    def maxSlidingWindow(self, nums, k):
        l=0
        r=0
        maxi=[]
        ans=[]
        n=len(nums)
        while r<n:
            print(maxi)
            while len(maxi)>0 and maxi[-1]<nums[r]:
                maxi.pop()
            maxi.append(nums[r])
            
            if r-l+1<k:
                r+=1
            
            else:
                ans.append(maxi[0])
                if maxi[0]==nums[l]:
                    maxi.pop(0)
                l+=1
                r+=1
        return ans


s1 = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(s1.maxSlidingWindow(nums,k))

    


