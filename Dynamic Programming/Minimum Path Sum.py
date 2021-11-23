#Recursion O(2^N APPROACH)
class Solution:
    def help(self,grid,i,j,m,n):
        if i==m-1 and j==n-1:
            return grid[i][j]
        if i>=m or j>=n:
            return sys.maxsize
        left=grid[i][j]+self.help(grid,i+1,j,m,n)
        right=grid[i][j]+self.help(grid,i,j+1,m,n)
    

        return min(left,right)
    def minPathSum(self, grid: List[List[int]]) -> int:
        i=0
        j=0
        m=len(grid)
        n=len(grid[0])
        return self.help(grid,i,j,m,n)
   
        
#Dp Top down Approach O(M*N) with recursion call stack space
class Solution:
    def help(self,grid,i,j,m,n,dp):
        if i==m-1 and j==n-1:
            return grid[i][j]
        if i>=m or j>=n:
            return sys.maxsize
        if dp[i][j]!=-1:
            return dp[i][j]
        left=grid[i][j]+self.help(grid,i+1,j,m,n,dp)
        right=grid[i][j]+self.help(grid,i,j+1,m,n,dp)
        dp[i][j] =min(left,right)
        return min(left,right)
    
    

    def minPathSum(self, grid: List[List[int]]) -> int:
        i=0
        j=0
        m=len(grid)
        n=len(grid[0])
        dp=[[-1 for i in range(n+1)]for j in range(m+1)]
        return self.help(grid,i,j,m,n,dp)
   
 #Dp Bottom up O(M*N) wit no call stack space
class Solution:
    def min_cost_path(self,grid,i,j,m,n,dp):
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    dp[i][j]=grid[i][j]
                elif i==m-1:
                    dp[i][j]=grid[i][j]+dp[i][j+1]

                elif j==n-1:
                    dp[i][j]=grid[i][j]+dp[i+1][j]
                
                else:
                    dp[i][j]=grid[i][j]+min(dp[i+1][j],dp[i][j+1])
                    
        return dp[0][0]
                

    def minPathSum(self, grid: List[List[int]]) -> int:
        i=0
        j=0
        m=len(grid)
        n=len(grid[0])
        dp=[[-1 for i in range(n)]for j in range(m)]
        return self.min_cost_path(grid,i,j,m,n,dp)
   
        
