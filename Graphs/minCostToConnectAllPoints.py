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
    # TC:- O(ELOGE)
    # SC: O(E) + O(V+E) + O(V)
    def minCostConnectPoints(self, points):
        V=len(points)
        adj= [[] for _ in range(V)]

        for i in range(0,V):
            x1,y1 = points[i]

            for j in range(0,V):
                x2,y2= points[j]
                if i!=j:
                    cost = abs(x1-x2)+abs(y1-y2)

                    adj[i].append((j,cost))
        
        
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
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(s1.minCostConnectPoints(points))

    


