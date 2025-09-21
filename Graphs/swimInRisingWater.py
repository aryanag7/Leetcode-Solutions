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

import heapq
class Solution:
    # TC:- O(ELOGV) - o(n * m * 4 log (n *  m))
    # SC:- O(N*M) + O(N*M)
    def swimInWater(self, grid):
        n= len(grid)
        m=len(grid[0])

        visited = [[0 for j in range(m)] for i in range(n)]
        visited[0][0] = 1

        pq = [(grid[0][0],(0,0))]

        while len(pq)>0:
            time, (i,j) = heapq.heappop(pq)

            if i==n-1 and j==m-1:
                return time

            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]

                if new_i>=0 and new_i<n and new_j>=0 and new_j<m and visited[new_i][new_j]==0:
                    
                    new_elevation = max(time, grid[new_i][new_j])
                    heapq.heappush(pq, (new_elevation,(new_i,new_j)))
                    visited[new_i][new_j] = 1
        


s1 = Solution() 
grid = grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(s1.swimInWater(grid))

    


