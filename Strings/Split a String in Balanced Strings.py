class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans=0
        bal=0
        for i in range(0,len(s)):
            if s[i]=="L":
                bal=bal+1
            elif s[i]=="R":
                bal=bal-1
            if bal==0:
                    
                ans=ans+1
               
        return ans
