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
    def isConnected(self,src ,dst, adj,visited):
        if src == dst:
            return True


        visited[src]=1

        for ch in adj[src]:
            if visited[ch]==0:
                if self.isConnected(ch ,dst, adj,visited):
                    return True
        
        return False




    # TC:- O(E×(V+E))
    def findRedundantConnection(self, edges):
        n= len(edges)
        adj = [[] for _ in range(n)]

        for edge in edges:
            u= edge[0]
            v= edge[1]

            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        for i in range(n-1,-1,-1):
            u =  edges[i][0]
            v = edges[i][1]

            adj[u-1].remove(v-1)
            adj[v-1].remove(u-1)
            visited = [0]*n

            if self.isConnected(u-1 ,v-1, adj,visited):
                return edges[i]
            
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)

            


        
        

        
        


s1 = Solution() 
edges =  [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(s1.findRedundantConnection(edges))

    


