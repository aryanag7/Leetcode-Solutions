import bisect
import sys
import os
import math
from collections import defaultdict
from collections import Counter
from typing import Deque
from collections import deque
from itertools import accumulate

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Redirect stdin and stdout
sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')



class Solution:
    def Dfs_traversal(self,i,j,n,m,grid,visited):
        visited[i][j]=1

        directions = [(-1,0), (0,-1),(1,0),(0,1)]

        for d in directions:
            new_i = i +d[0]
            new_j = j+d[1]

            if new_i>=0 and new_i<n and new_j>=0 and new_j<m and grid[new_i][new_j]=="1" and visited[new_i][new_j]==0:
                self.Dfs_traversal(new_i,new_j,n,m,grid,visited)


    # TC:- O(N * M * 4)
    # SC:- O(n*m) visited + O(n * m) stack space
    def numIslands(self, grid):
        n=len(grid)
        m=len(grid[0])

        visited = [[0 for j in range(m)] for i in range(n)]

        numOfIslands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and visited[i][j]==0:
                    self.Dfs_traversal(i,j,n,m,grid,visited)
                    numOfIslands+=1
                

        return numOfIslands


 


        

        
        


    
s1 = Solution()
grid = [
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","1"]
]
print(s1.numIslands(grid))

    


