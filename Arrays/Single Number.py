class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        element=0
        for i in range(0,len(nums)):
            element=element^nums[i]
        return element
        
