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
    def isValid(self,n,m,i,j,visited):
        return i<n and i>=0 and j>=0 and j<m and visited[i][j]==0 
    

    # TC:- O(N * M * 4) if all oranges fresh and in 4 directions
    # SC:- O(N * M) for queue if all rotten, O(N * M) for visited
    def orangesRotting(self, grid):
        n=len(grid)
        m=len(grid[0])
        visited = [[0 for j in range(m)] for i in range(n)]
        freshCount = 0

        queue=[]
        for i in range(0,n):
            for j in range(0,m):
                #start off with all rotten oranges at level 0
                if grid[i][j]==2:
                    queue.append(((i,j),0))
                    visited[i][j]=1

                elif grid[i][j]==1:
                    freshCount+=1
        
        t=0
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        while len(queue)>0:
            (i,j), level = queue.pop(0)
            t= max(t, level)

            for d in directions:
                new_i = i+d[0]
                new_j = j+d[1]

                if self.isValid(n,m,new_i,new_j,visited) and grid[new_i][new_j]==1:
                    freshCount-=1
                    queue.append(((new_i,new_j),level+1))
                    visited[new_i][new_j]=1
        

        #can also have a freshCount and increment and decrement respectively
        # for i in range(0,n):
        #     for j in range(0,m):
        #         if visited[i][j]==0 and grid[i][j]==1:
        #             return -1
        
        if freshCount>0:
            return -1

        return t







        

        
        

   


   

    
s1 = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(s1.orangesRotting(grid))

    


