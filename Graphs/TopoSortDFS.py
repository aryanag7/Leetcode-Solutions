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
    def  Dfs(self,src, visited, adj, stack):
        visited[src]=1

        for ch in adj[src]:
            if visited[ch]==0:
                self.Dfs(ch, visited, adj, stack)
        
        stack.append(src)



    def topoSort(self, V, E,  edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u=edge[0]
            v=edge[1]
            adj[u].append(v)
        
        visited = [0]*V
        stack=[]

        for i in range(0,V):
            if visited[i]==0:
                self.Dfs(i, visited, adj, stack)
        
        ans= []
        while stack:
            ans.append(stack.pop())
        

        return ans
        


    
s1 = Solution() 
V = 4
E = 3
edges = [[3, 0], [1, 0], [2, 0]]
print(s1.topoSort(V, E, edges))

    


