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
    # def longestOnes(self, nums, k):
    #     ans=0

    #     n=len(nums)
    #     for i in range(0,n):
    #         zerosCount=0
    #         for j in range(i,n):
    #             if nums[j]==0:
    #                 zerosCount+=1
    #                 if zerosCount>k:
    #                     break
                       
    #             ans= max(ans, j-i+1)
        
        # return ans



    
    # TC:- O(N+N)
    # SC:- O(1)
    def longestOnes(self, nums, k):
        l=0
        r=0
        ans=0
        zerosCount=0
        n=len(nums)

        while r<n:
            if nums[r]==0:
                zerosCount+=1
            
            while zerosCount>k:
                if nums[l]==0:
                    zerosCount-=1
                l+=1
            

            #valid window
            ans = max(ans, r-l+1)
            r+=1
        
        return ans
    


    #optimization over the above code - as number of zeros will increase just by 1 when window is invalid, lets say zeros is 2  and k=2 so,
    # zeros<=k but when new ele is 0 3<=2, we just need to remove one element from the left (potentially zero) to make it a valid window again and making sure that the WINDOW SIZE  dont go DOWN BEYOND our ans length (IMPPPPPP). we will increase it if condition satisified but will not let it go beyond what we found ansgit 

    # TC:- O(N)
    # SC:- O(1)
    def longestOnes(self, nums, k):
        l=0
        r=0
        ans=0
        zerosCount=0
        n=len(nums)

        while r<n:
            if nums[r]==0:
                zerosCount+=1
            
            if zerosCount>k:
                if nums[l]==0:
                    zerosCount-=1
                l+=1
            

            #maybe invalid
            if zerosCount<=k:
                ans = max(ans,r-l+1)

            r+=1
        
        return ans



        




            
 


s1 = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(s1.longestOnes(nums,k))

    


