Approach 1: TC: O(N^2) As for traversing the dictionar we need O(N) and for inserting it into dictionary we need O(N) .

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dict={}
        for i in range(0,len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        n=len(dict.keys())
        for i,key in enumerate(dict.keys()):
            nums[i]=key    
        return n
Approach 2:TC : O(N)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        while j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                i=i+1
                nums[i]=nums[j]
                j+=1
        return i+1
