class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ans=0
        stack=[]
        for i in range(0,len(S)):
            if S[i]=="(":
                stack.append(S[i])
                ans+=1
            else:
                if len(stack)>0 and stack[-1]=="(":
                    stack.pop()
                    ans-=1
                else:
                    stack.append(S[i])
                    ans+=1
        
        return ans    
