#Approach 1 Linear Search or min() O(N)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
        
#Approach 2 Binary Search O(LOGN)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low<high:
            mid=low+(high-low)//2
            if nums[mid]>nums[-1]:
                low=mid+1
            else:
                high=mid
        return nums[low]
                
                
        
