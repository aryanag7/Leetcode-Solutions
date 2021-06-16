class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        ans=0
        for i in range(0,len(s)):
            if s[i]=="(":
                count=count+1
        
            elif s[i]==")":
                count=count-1
            ans=max(ans,count)      
        return ans          
        
