class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans=0
        for i in range(0,len(startTime)):
            if queryTime>=startTime[i] and queryTime<= endTime[i]:
                ans=ans+1
  


        return ans
