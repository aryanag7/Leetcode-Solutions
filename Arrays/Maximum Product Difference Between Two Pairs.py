class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
       
        product1=nums[-1]*nums[-2]
        product2=nums[0]*nums[1]
        ans=product1-product2
        return ans
