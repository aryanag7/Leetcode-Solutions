class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and i<j:
                    count=count+1
        return count    
    # 2nd answer
     nums=sorted(nums)
        dict=Counter(nums)
        ans=0
        for val in dict.values():
            ans=ans+(val**2-val)//2
        return ans    
        
