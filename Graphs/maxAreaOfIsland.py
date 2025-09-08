import bisect
import sys
import os
import math
from collections import defaultdict
from collections import Counter
from typing import Deque
from collections import deque
from itertools import accumulate
import heapq

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Redirect stdin and stdout
sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')



class Solution:
    # TC:- O(N*M*4)
    # SC:- O(N*M)
    def Dfs_traversal(self,grid, i, j,n,m, visited):
        
        visited[i][j]=1

        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        count=1
        for d in directions:
            new_i = i+d[0]
            new_j = j+d[1]

            if new_i>=0 and new_i<n and new_j>=0 and new_j<m and grid[new_i][new_j]==1 and visited[new_i][new_j]==0:
                count += self.Dfs_traversal(grid, new_i, new_j,n,m, visited)
                
        
        return  count



    def maxAreaOfIsland(self, grid):
        n=len(grid)
        m=len(grid[0])

        visited = [[0 for j in range(m)] for i in range(n)]

        maxArea = 0 

        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j]==1 and visited[i][j]==0:
                    count = self.Dfs_traversal(grid, i, j,n,m, visited)
                    maxArea = max(maxArea, count)
        

        return maxArea
        








s1 = Solution() 
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(s1.maxAreaOfIsland(grid))

    


