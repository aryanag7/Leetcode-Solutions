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
    # TC:- O(ELOGE)+ O(ELOGE) - HEAP SIZE O(E)
    # SC:- O(E) + O(V)
    def spanningTree(self, V, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u=edge[0]
            v= edge[1]
            wt = edge[2]

            adj[u].append((v,wt))
            adj[v].append((u,wt))
        
        visited = [0]*V
        pq=[(0,0)]


        s=0
        while len(pq)>0:
            wt, node = heapq.heappop(pq)

            #means that this node with this specific edge weight is ignored as the minimum edge with this node has already been taken
            if visited[node]==1:
                continue

            visited[node]=1
            s+=wt

            for ch in adj[node]:
                if visited[ch[0]]==0:
                    heapq.heappush(pq, (ch[1],ch[0]))
        
        return s







s1 = Solution() 
V = 3
E = 3
Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
print(s1.spanningTree(V,Edges))

    


