class Solution:
    def __max_sub_subarray(self,nums,target,k):
        i=0
        sum=0
        while i<k:
            sum+=nums[i]
            i+=1
        l=0
        r=k
        maxi=sum
        while r<len(nums):
            sum-=nums[l]
            l+=1

            sum+=nums[r]
            r+=1

            maxi=max(maxi,sum)
        return maxi
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=1
        high=len(nums)
        anspossible=False
        while low<=high:
            mid=low+(high-low)//2
            max_sum=self.__max_sub_subarray(nums,target,mid)
            if max_sum<target:
                low=mid+1
            else:
                anspossible=True
                high=mid-1
                
        if anspossible==True:
            return low
        return 0
