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



class Solution:
    """
    In a Directed Acyclic Graph (DAG), edges always go forward (no cycles).

    Topological sort gives an order of nodes such that all edges go from left to right.

    This order ensures:
     When we process a node, we have already computed the shortest distance to it.
     So, we can safely “relax” (update) its outgoing edges without missing any shorter path.


    
    Can be solved using simple BFS, but it might take some moire time/iterationbs to update the dist of a node to the shortest as we might take a node which is longer from the queue (based on FIFO) which updated further with longer distances (as its still less than infinity) but ultimately we will process the nodes with shorter distances updating its children with more shorter distances, re- relaxations (update) wil be required 
    
    """
    def  TopoDfs(self,src, visited, adj, stack):
        visited[src]=1

        for ch in adj[src]:
            if visited[ch[0]]==0:
                self.TopoDfs(ch[0], visited, adj, stack)
        
        stack.append(src)


    def shortestPath(self, V, E, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u= edge[0]
            v= edge[1]
            wt = edge[2]

            adj[u].append((v,wt))


        #plain topo sort O(V+E)
        stack = []
        visited = [0]*V
        for i in range(0,V):
            if visited[i]==0:
                self.TopoDfs(i , visited, adj, stack)
        
   
        
        dist = [float('inf')]* V
        src=4

        while stack[-1]!=src:
            stack.pop()

        dist[src]=0
        # O(V+E)
        while len(stack)>0:
            node = stack.pop()

            for ch in adj[node]:
                if dist[node]+ch[1]< dist[ch[0]]:
                    dist[ch[0]] = dist[node] + ch[1]
        
        
        for i in range(0,V):
            if dist[i]==float('inf'):
                dist[i]=-1
        
        return dist




s1 = Solution() 
V = 6
E = 7
edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]]
print(s1.shortestPath(V, E, edges))

    


