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
    #multi source shortest path
    # TC:- O(N^3)
    #SC:- O(N * N) - using matrix to solve the problem
    def floydWarshall(self, dist):
        n = len(dist)


        for via in range(0,n):
            for i in range(0,n):
                for j in range(0,n):
                    if dist[i][via]!=1e8 and dist[via][j]!=1e8:
                        viaPath = dist[i][via] + dist[via][j]
                        dist[i][j] = min(dist[i][j], viaPath)

        #if there is any negative cycle in it
        for i in range(0,n):
            if dist[i][i]<0:
                return "negative cycle"

        return dist


s1 = Solution() 
dist = [[0, 4, 108, 5, 108], [108, 0, 1, 108, 6], [2, 108, 0, 3, 108], [108, 108, 1, 0, 2], [1, 108, 108, 4, 0]]
print(s1.floydWarshall(dist))

    


