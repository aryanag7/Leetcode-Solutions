class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict={}
        for i in range(len(nums)):

            if nums[i] not in dict:
                dict[nums[i]]=1
            else:
                dict[nums[i]]+=1
    
        ans=0
        for i in dict:
            if dict[i]<2:
                ans=ans+i
        return ans        
    
        
