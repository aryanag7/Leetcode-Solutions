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
    # TC:- O(N * M * 4)
    # SC:- O(N * M) + O(n* m)
    def shortestPath(self, grid , source , destination):
        n = len(grid)
        m= len(grid[0])

        src_i = source[0]
        src_j = source[1]

        dest_i = destination[0]
        dest_j = destination[1]

        dist = [[float('inf') for j in range(m)] for i in range(n)]

        queue = [((src_i,src_j),0)]

        while len(queue)>0:
            (i,j), steps = queue.pop(0)
            if i== dest_i and j==dest_j:
                return steps

            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            for d in directions:
                new_i = i +d[0]
                new_j = j +d[1]

                new_dist  = steps+1



                if new_i>=0 and new_i<n and new_j>=0 and new_j<m and grid[new_i][new_j]==1 and new_dist< dist[new_i][new_j]:
                    dist[new_i][new_j] = new_dist
                    queue.append(((new_i,new_j), new_dist ))
        
        return -1 
                                



        
        

s1 = Solution() 
grid =     [[1, 1, 1, 1,1],
            [1, 1, 1,1, 1],
            [1, 1, 1, 0,0],
            [1, 0, 0, 1,1]]
source = [0,0]
destination = [3,4]
print(s1.shortestPath(grid,source, destination))

    


