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

    def Dfs_traversal(self,sr_i,sr_j,n,m,grid,visited,coordinates,init_i,init_j):
        visited[sr_i][sr_j]=1
        coordinates.append(( sr_i - init_i , sr_j - init_j ))

        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        for d in directions:
            new_i = sr_i+d[0]
            new_j = sr_j+d[1]

            if new_i>=0 and new_i<n and new_j>=0 and new_j<m and grid[new_i][new_j]==1 and visited[new_i][new_j]==0:
                self.Dfs_traversal(new_i,new_j,n,m,grid,visited,coordinates,init_i,init_j)



    # TC:- O(N * M) outer loop + O(N * M * 4) max number of dfs calls if all 1's 
    # SC:- O(N* M) for visited and O(N * M) worst case all coordinates stored in set
    def numDistinctIslands(self, grid):
        n=len(grid)
        m=len(grid[0])

        visited = [[0 for j in range(m)] for i in range(n)]

        distinct_islands = set()

        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j]==1 and visited[i][j]==0:
                    coordinates = []
                    self.Dfs_traversal(i,j,n,m,grid,visited,coordinates,i,j)
                    distinct_islands.add(tuple(coordinates))



        return len(distinct_islands)


        
        


        


    
s1 = Solution() 
grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(s1.numDistinctIslands(grid))

    


