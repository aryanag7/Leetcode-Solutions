import math
class Solution:
    def help(self,n,dp):
        if n==1:
            return False
        if dp[n]!=-1:
            return dp[n]
        num=int(math.sqrt(n))
        for i in range(1,num+1):
            if n%i==0:
                
                if self.help(n-i,dp)==False:
                    dp[n]=True
                    return True
                
        dp[n]=False
        return False
    def divisorGame(self, n: int) -> bool:
        dp=[-1]*(n+1)
        return self.help(n,dp)
        
        
#Approach 2
return n%2==0
