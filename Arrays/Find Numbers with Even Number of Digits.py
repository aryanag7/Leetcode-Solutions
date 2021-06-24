class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        ans=0
        for i in range(0,len(nums)):
       
            if len(str(nums[i]))%2==0:
                ans=ans+1
        return ans    
      
      
      
         even = 0
         for num in nums:
            
            digits = 0
            while num > 0:
              num //= 10
              digits += 1
           if digits % 2 == 0:
              even += 1
        return even 
