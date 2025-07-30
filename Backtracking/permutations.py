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

    # TC:- O(N! * N)
    # SC:- O(N) stack space, O(N) map array
    # def permute(self, nums):
    #     ans=[]
    #     n=len(nums)
    #     track= [False]*n

    #     def permuteHelper(nums,ds,n):
    #         if len(ds)==n:
    #             ans.append(ds)
    #             return


    #         for i in range(0,len(nums)):
    #             if track[i]==False:
    #                 track[i]=True
    #                 permuteHelper(nums,ds+[nums[i]],n)
    #                 track[i]=False

    #     permuteHelper(nums,[],n)

    #     return ans
    



    # here TC remains the same but we are not using any extra visited array just in place swapping. 
    # Trying to start every number from each position, say  1,2,3 each from position 1 then 2,3 each from position2 
    def permute(self, nums):
        ans=[]
        n=len(nums)

        def permuteHelper(nums,ind,ds,n):
            if len(ds)==n:
                ans.append(ds)
                return 
            
            for i in range(ind,n):
                nums[ind],nums[i]=nums[i],nums[ind]
                
                permuteHelper(nums,ind+1, ds+[nums[ind]],n)

                nums[ind],nums[i]=nums[i],nums[ind]
        
        
        permuteHelper(nums,0,[],n)

        return ans
    
        

     


        


s1 = Solution()
nums = [1,2,3]
print(s1.permute(nums))

    


