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
    #same as surrounded regions question, just need to count the enclosed cells- used BFS here instead of DFS in previous
    # TC:- O(N * M * 4)
    # SC:- O(N *M)
    def numEnclaves(self, grid):
        n=len(grid)
        m=len(grid[0])

        visited= [[0 for j in range(m)] for i in range(n)]
        queue=[]

        for j in range(0,m):
            if grid[0][j]==1:
                queue.append((0,j))
                visited[0][j]=1
            
            if grid[n-1][j]==1:
                queue.append((n-1,j))
                visited[n-1][j]=1
        
        for i in range(0,n):
            if grid[i][0]==1:
                queue.append((i,0))
                visited[i][0]=1
            
            if grid[i][m-1]==1:
                queue.append((i,m-1))
                visited[i][m-1]=1

        
        while len(queue)>0:
            i,j = queue.pop(0)

            directions = [(-1,0),(0,-1),(1,0),(0,1)]

            for d in directions:
                new_i = i +d[0]
                new_j = j + d[1]

                if new_i>=0 and new_i<n and new_j>=0 and new_j<m and visited[new_i][new_j]==0 and grid[new_i][new_j]==1:
                    queue.append((new_i,new_j))
                    visited[new_i][new_j]=1
        
        count=0
        for i in range(n):
            for j in range(m):
                if visited[i][j]==0 and grid[i][j]==1:
                    count+=1
                    
        
        return count
        

        


    
s1 = Solution() 
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(s1.numEnclaves(grid))

    


