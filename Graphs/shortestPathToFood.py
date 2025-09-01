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
    # TC:- O(N * M * 4)
    # SC:- O(N *M) + O(N* M)
    def getFood(self, grid):
        n = len(grid)
        m=len(grid[0])

        visited= [[0 for j in range(m)] for i in range(n)]
        queue=[]

        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j]=="*":
                    queue.append(((i,j),0))
        
        while len(queue)>0:
            (i,j), steps = queue.pop(0)

            if grid[i][j]=="#":
                return steps

            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            for d in directions:
                new_i = i +d[0]
                new_j = j +d[1]

                if new_i>=0 and new_i<n and new_j>=0 and new_j<m and visited[new_i][new_j]==0 and grid[new_i][new_j]!="X":
                    queue.append(((new_i,new_j),steps+1))
                    visited[new_i][new_j]=1
        
        return -1








    
s1 = Solution() 
grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["O","O","O","O","O","O","O","O"]]
print(s1.getFood(grid))

    


