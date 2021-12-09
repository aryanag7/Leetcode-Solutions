class Solution:
    def arrangeCoins(self, n: int) -> int:
        low=1
        high=n
        ans=0
        while low<=high:
            mid=low+(high-low)//2
            row_coins=mid*(mid+1)//2
            
            if row_coins>n:
                high=mid-1
            else:
                ans=mid
                low=mid+1
        return ans
