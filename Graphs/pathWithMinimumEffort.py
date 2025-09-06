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
    # TC:- O(E LOG(V)), in a grid E would be n * m * 4 and V is n * m
    # SC:- O(N*M) + O( N*M)
    def minimumEffortPath(self, heights):
        n=len(heights)
        m=len(heights[0])

        effort =[[float('inf') for _ in range(m)] for _ in range(n)]
        effort[0][0]=0

        pq =[(0,(0,0))]

        while len(pq)>0:
            diffTillNow, (i,j) = heapq.heappop(pq)

            if i==n-1 and j==m-1:
                return diffTillNow
            
            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            for d in directions:
                new_i = i + d[0]
                new_j = j+ d[1]

                if new_i>=0 and new_i<n and new_j>=0 and new_j<m:
                    curr_diff = abs(heights[i][j] - heights[new_i][new_j])
                    maxi = max(diffTillNow, curr_diff)

                    if maxi < effort[new_i][new_j]:
                        effort[new_i][new_j] = maxi
                        heapq.heappush(pq, (maxi, (new_i,new_j)))

  

s1 = Solution() 
heights = [[1,2,3],[3,8,4],[5,3,5]]
print(s1.minimumEffortPath(heights))

    


