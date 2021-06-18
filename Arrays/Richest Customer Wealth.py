class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum=0
        ans=0
        for row in accounts:
            for element in row:
                sum=sum+element
            ans=max(sum,ans)  
            sum=0
                
        return ans
