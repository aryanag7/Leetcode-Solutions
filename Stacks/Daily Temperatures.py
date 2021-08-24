class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*len(temperatures)
        stack=[]
        stack.append([temperatures[n-1],n-1])
        for i in range(len(temperatures)-2,-1,-1):
            while len(stack)!=0 and stack[-1][0]<=temperatures[i]:
                stack.pop()
            if len(stack)==0:
                ans[i]=0
            else:
                ans[i]=abs(i-stack[-1][1])
            stack.append([temperatures[i],i])
        return ans

        
