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
    # TC:- O(V+E) 
    # SC:- O(V) + O(V)
    #IF there are V nodes and E edges then,
    # -> if E = V-1 , every node can visit every other node, no cycles, connected
    # -> If E is more than that, it has cycles.
    # -> If E is less than V-1 which means its disconnected, to be 1 component it needs to have alteast V-1 edges
    def Dfs_traversal(self,src, adj, visited):
        visited[src]=1

        for ch in adj[src]:
            if visited[ch]==0:
                self.Dfs_traversal(ch,adj,visited)



    def validTree(self, n, edges):
        numberOfEdges = len(edges)
        adj = [[] for _ in range(n)]
        for edge in edges:
            u=edge[0]
            v=edge[1]

            adj[u].append(v)
            adj[v].append(u)

        visited = [0]*n
        components = 0
        for i in range(0,n):
            if visited[i]==0:
                self.Dfs_traversal(i, adj, visited)
                components+=1

        if components==1 and numberOfEdges+1 == n:
            return True
        
        return False
        


    


        
        

s1 = Solution() 
n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
print(s1.validTree(n,edges))

    


