class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi=0
        max_ones=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                max_ones+=1
                maxi=max(maxi,max_ones)
            if nums[i]==0:
                max_ones=0
        return maxi
      
