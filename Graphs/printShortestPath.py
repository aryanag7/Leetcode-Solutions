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
    def shortestPath(self,n, m, edges):
        adj= [[] for _ in range(n+1)]
        for edge in edges:
            u=edge[0]
            v=edge[1]
            wt = edge[2]

            adj[u].append((v,wt))
            adj[v].append((u,wt))

        src =1 
        dist = [float('inf')]*(n+1)
        parent = [-1]*(n+1)
        
        pq = [(0,src)]
        dist[src]=0

        while len(pq)>0:
            curr_dist, node = heapq.heappop(pq)

            for ch    in adj[node]:
                child = ch[0]
                wt = ch[1]
                new_dist = curr_dist + wt

                if new_dist < dist[child]:
                    dist[child] = new_dist
                    heapq.heappush(pq, (new_dist, child))
                    parent[child] = node
        
        if dist[n]==float('inf'):
            return [-1]
        
        
        # st=[]
        # st.append(n)
        # i=n
        # while i>=1:
        #     if parent[i]==-1:
        #         break
        #     st.append(parent[i])
        #     i = parent[i]
        
        # st.append(dist[n])
        
        # ans=[]
        # while len(st)>0:
        #     ans.append(st.pop())
        

        # return ans
    

        ans=[]
        ans.append(n)
        i=n
        while parent[i]!=-1:
            ans.append(parent[i])
            i = parent[i]


        
        ans= ans[::-1]
        return ans




        
        

s1 = Solution() 
n = 5
m= 6,
edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
print(s1.shortestPath(n,m,edges))

    


