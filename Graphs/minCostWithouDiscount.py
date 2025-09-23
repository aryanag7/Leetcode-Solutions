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
    def minimumCost(self, n, highways,  discounts):
        adj = [[] for _ in range(n)]
        for edge in highways:
            u = edge[0]
            v = edge[1]
            wt = edge[2]

            adj[u].append((v,wt))
            adj[v].append((u,wt))

    
        
        INF = float('inf')  
        dist = [ [INF] * (discounts+1) for _ in range(n)]
        dist[0][discounts] = 0

    

        pq = [(0, 0, discounts)]

        while len(pq)>0:
            d, node, discountsLeft = heapq.heappop(pq)

            # if node == n-1:
            #     print(distWithDiscount,distWithoutDiscount)
            #     return dist
            if node == n-1:
                return d

            for chNode, wt in adj[node]:

                #with discounts - IF LEFT
                if discountsLeft > 0:
                    new_dist = d + (wt//2)
                    if new_dist < dist[chNode][discountsLeft-1]:
                        dist[chNode][discountsLeft-1] = new_dist
                        heapq.heappush(pq, (new_dist, chNode, discountsLeft-1))

                #without discount
                new_dist = d + wt
                if new_dist< dist[chNode][discountsLeft]:
                    dist[chNode][discountsLeft] = new_dist
                    heapq.heappush(pq, (new_dist, chNode, discountsLeft))

      
        
        return -1




s1 = Solution() 
n = 6
highways = [[0,1,2],[1,3,4],[0,2,6],[2,3,8],[3,4,100],[4,5,200]]
discounts = 2
print(s1.minimumCost(n, highways, discounts))

    


