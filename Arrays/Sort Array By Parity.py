class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #sol 1
        even=[]
        odd=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        return even+odd   
        #sol 2
        nums.sort(key=lambda x:x%2)
        return nums
       #sol 3
        even=0
        odd=0
        while even<len(nums):
            if nums[even]%2==0:
                temp=nums[even]
                nums[even]=nums[odd]
                nums[odd]=temp
                even=even+1
                odd=odd+1

            else:
                even=even+1   
        return nums
          
