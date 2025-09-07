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
    # TC:- O(V-1 * E )
    # sc:- O( V)
    def bellmanFord(self, V, edges, src):
        dist = [float('inf')]*V
        dist[src]=0

        for i in range(0,V-1):
            for edge in edges:
                u= edge[0]
                v=edge[1]
                wt = edge[2]

                if dist[u]!= float('inf') and  dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        
        #to check if there is any negative cycle - it will still reduce weight on the Nth iteration although we would have had the shortest path in N-1 iterations
        for edge in edges:
            u= edge[0]
            v=edge[1]
            wt = edge[2]

            if dist[u]!= float('inf') and  dist[u] + wt < dist[v]:
                return [-1]


        
        return dist


    


        
        

s1 = Solution() 
V = 5
edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
src = 0
print(s1.bellmanFord(V,edges, src))

    


