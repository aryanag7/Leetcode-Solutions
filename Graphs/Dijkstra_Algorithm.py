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
    # TC: - O(E LOG(V)) WORST CASE E IS NUMBER OF EDGES AND V ARE VERTICIES
    # SC:- O(V)  + O(V) 
    def dijkstra(self, V, edges, src):
        dist = [float('inf')]*V

        adj = [[] for _ in range(V)]
        for edge in edges:
            u=edge[0]
            v=edge[1]
            wt = edge[2]

            adj[u].append((v,wt))
            adj[v].append((u,wt))

        pq = [(0,src)]
        dist[src]=0

        # E = V^2

        # total nodes in pq - V
        while len(pq)>0:
            curr_dist, node = heapq.heappop(pq)

            #imagine for a graph worst possible number of edges, it would be V-1 for a dense graph where every node is connected to every other node in the graph
            for ch    in adj[node]:
                child = ch[0]
                wt = ch[1]
                new_dist = curr_dist + wt

                if new_dist < dist[child]:
                    dist[child] = new_dist
                    heapq.heappush(pq, (new_dist, child))
        
        return dist

        
        







s1 = Solution() 
V = 3
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2
print(s1.dijkstra(V,edges,src))

    


