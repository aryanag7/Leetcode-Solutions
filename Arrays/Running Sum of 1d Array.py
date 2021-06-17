class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
#          for i in range(1,len(nums)):
#                 nums[i]=nums[i]+nums[i-1]
#         return nums  

          a=list(map(int,input().split()))
          ans=[]
          ans.append(a[0])
          for i in range(1,len(a)):
          
              ans.append(ans[i-1]+a[i])
          print(ans)    
      
      
