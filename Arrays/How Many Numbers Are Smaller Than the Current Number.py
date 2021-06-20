class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer=[]*len(nums)
        count=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i]>nums[j]:
                    count=count+1
            answer.append(count)
            count=0
        return answer    
      #2nd answer o(nlogn)
      duplicate=sorted(nums)
    dict={}
    for i in range(len(duplicate)):
        if duplicate[i] in dict:
            continue
        else:
            dict[duplicate[i]]=i
    answer=[]
    for i in nums:
        if i in dict:
            answer.append(dict[i])
    return answer     
