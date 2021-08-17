class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        count=0
        stack=[]
        for i in s:
            if i=="(":
                stack.append(i)
                count+=1
                ans=max(count,ans)
            if i==")":
                if stack[-1]=="(":
                    stack.pop()
                    count-=1
            ans=max(count,ans)
                    
        return ans
     
        
