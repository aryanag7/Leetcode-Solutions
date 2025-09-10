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
    # TC:- O(E LOGV) + O(N)
    # SC:- O(V)+ O(V)+ O(V)
    def networkDelayTime(self, times, n, k):
        dist = [float('inf')]*(n+1)

        adj =[[] for _ in range(n+1)]

        for time in times:
            u=time[0]
            v=time[1]
            t = time[2]

            adj[u].append((v,t))

        pq = [(0,k)]
        dist[k]=0
        while len(pq)>0:
            time, node = heapq.heappop(pq)

            for ch in adj[node]:
                if time + ch[1] < dist[ch[0]]:
                    dist[ch[0]] = time + ch[1]
                    heapq.heappush(pq, (time+ch[1],ch[0]))
        
        
        maxi = -1
        for i in range(1,n+1):
            if dist[i]==float('inf'):
                return -1
            maxi = max(maxi , dist[i])
        
        return maxi


s1 = Solution() 
times = [[1,2,1]]
n = 2
k = 2
print(s1.networkDelayTime(times,n,k))

    


