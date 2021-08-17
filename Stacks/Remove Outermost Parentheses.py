class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count=0
        ans=""
        
        for i in S:
            if i=="(":
                count+=1
                if count>=2:
                    ans=ans+"("
            elif i==")":
                count-=1
                if count>=1:
                    ans=ans+")"
        return ans
        
        
