#Approach1 O(N^2)
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        for i in range(0,len(nums)):
            sum=0
            for j in range(i,len(nums)):
                sum+=nums[j]
                maxi=max(maxi,sum)
        return maxi
        
#Approach2 Kadane's Algo O(N)
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        curr_sum=0
        for i in range(0,len(nums)):
            curr_sum+=nums[i]
            if curr_sum>maxi:
                maxi=curr_sum
            if curr_sum<0:
                curr_sum=0
        
     
        return maxi

