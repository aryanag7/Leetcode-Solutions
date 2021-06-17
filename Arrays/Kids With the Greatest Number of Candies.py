class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=max(candies)
        ans=[False]*len(candies)
        for i in range(0,len(candies)):
            if candies[i]+extraCandies>=maximum:
                ans[i]=True
            else:
                continue
        return ans 
