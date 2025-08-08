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

    # TC:- O(N^3* KLOGK ~ since k is 3 so no sorting complexity)
    # SC:- O(M) m-> unique triplets
    # Output triplets are at most O(n^3)  if all the triplets are valid

    def threeSum(self, nums):
        uniqueTriplets = set()

        n=len(nums)
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if nums[i] + nums[j]+ nums[k] == 0:
                        triplet = tuple(sorted((nums[i],nums[j],nums[k]))
                        )
                        uniqueTriplets.add(triplet)
        
        ans=[]
        for triplet in uniqueTriplets:
            ans.append(triplet)

        return ans



    
    # TC:- O(N^2)
    # SC:- ans -> O(M) m-> unique triplets, same for set and 
    # D is O(N)    
    def threeSum(self, nums):
        uniqueTriplets = set()

        n=len(nums)
        for i in range(0,n):
            d = defaultdict()
            for j in range(i+1,n):
                thirdNum = 0 - (nums[i]+nums[j])
                if thirdNum in d:
                    triplet = tuple(sorted((nums[i],nums[j],thirdNum)))
                    uniqueTriplets.add(triplet)

                d[nums[j]]=True

        ans=[]
        for triplet in uniqueTriplets:
            ans.append(triplet)

        return ans
    





    # TC:- O(NLOGN)+ O(n^2)
    
    # SC:- Output triplets are at most O(n²) because pairs after each fixed element sum up to O(n²) total.
    # also, tim sort used n space
    def threeSum(self, nums):
        ans=[]  
        n=len(nums)

        nums.sort()

        for i in range(0,n):
            if i>0 and nums[i]==nums[i-1]:
                continue

            j=i+1
            k=n-1

            while j<k:
                s= nums[i] + nums[j] +nums[k]

                if s<0:
                    j+=1
                
                elif s>0:
                    k-=1
                
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    
                    j+=1
                    k-=1
            
        return ans



s1 = Solution()
nums = [-1,0,1,2,-1,-4]
print(s1.threeSum(nums))
    

