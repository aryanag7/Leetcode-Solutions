class Solution: O(N^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
               
O(nlogn)
 nums.sort()
    
    i=0
    j=n-1
    while i<j:
        if nums[i]+nums[j]==target:
          return [i,j]
            
        elif nums[i]+nums[j]>target:
            j=j-1
        else:
            i=i+1
     
    
O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        
        dict={}
        for i in range(0,len(nums)):
            x=target-nums[i]
            if x in dict:
                return [dict[x],i]
            else:
                dict[nums[i]]=i
        
                  
    
