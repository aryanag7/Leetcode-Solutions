class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=[]
        ans.append(0)  
        ans.append(gain[0])
        for i in range(1,len(gain)):
            ans.append(ans[i]+gain[i])
        return max(ans)   
        
