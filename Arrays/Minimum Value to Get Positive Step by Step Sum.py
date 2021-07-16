class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        
        min_pos=min(nums)
        if min_pos>=0:
            return 1
        prefix_sum=[0]*len(nums)
        prefix_sum[0]=nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i]+=nums[i]+prefix_sum[i-1]
        ans=0
        for i in range(len(prefix_sum)):
            if prefix_sum[i]<ans:
                ans=prefix_sum[i]
        return abs(ans)+1


        
