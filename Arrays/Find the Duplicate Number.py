#dictionary approach
        
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for i in range(0,len(nums)):
            if dict[nums[i]]>1:
                return nums[i]
                            
#fast and slow pointer approach
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=nums[0]
        fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        fast=nums[0]
        while slow!=fast:
            fast=nums[fast]
            slow=nums[slow]
           
        return slow
