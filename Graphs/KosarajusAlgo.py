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
    def Dfs_traversal(self, src,adj, visited,  stack):
        visited[src]=1

        for ch in adj[src]:
            if visited[ch]==0:
                self.Dfs_traversal(ch, adj, visited, stack)
        
        stack.append(src)
    
    def Dfs_markVisited(self, src,adj, visited):
        visited[src]=1

        for ch in adj[src]:
            if visited[ch]==0:
                self.Dfs_markVisited(ch, adj, visited)
        
 



    # TC:- 3 * (V+E)
    # SC:- O(V)+O(V)+O(V+E) for revAdj
    def kosaraju(self, adj):
        V = len(adj)

        stack = []
        visited = [0]*V

        #O(V+E)
        for i in range(0,V):
            if visited[i]==0:
                self.Dfs_traversal(i,adj, visited,  stack)
        
        
        revAdj = [[] for _ in range(V)]

        #O(V+E)
        for i in range(0,V):
            visited[i]=0
            for ch in adj[i]:
                # edge is i -> ch
                revAdj[ch].append(i)
        

        components = 0
        #O(V+E)
        while len(stack)>0:
            node = stack.pop()

            if visited[node]==0:
                self.Dfs_markVisited(node, revAdj, visited)
                components+=1
        
        return components







         

        




s1 = Solution() 
adj= [[2, 3], [0], [1], [4], []]
print(s1.kosaraju(adj))

    


