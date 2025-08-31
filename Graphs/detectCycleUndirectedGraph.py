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
    #BFS
    def detectCycleBFS(self,src,adj,visited):
        queue = [(src,-1)]
        visited[src]=1

        while len(queue)>0:
            node, parent = queue.pop(0)

            for ch in adj[node]:
                if visited[ch]==0:
                    queue.append((ch,node))
                    visited[ch]=1
                else:
                    if ch != parent:
                        return True
        
        return False
    



    # TC:- O(V+2E)
    # SC:- O(V) + O(V) queue and visited, worst case no adjacent nodes outer for loop runs n times
    def isCycle(self, V,E, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u= edge[0]
            v= edge[1]
            adj[u].append(v)
            adj[v].append(u)

        visited = [0]*V

        for i in range(0,V):
            if visited[i]==0:
                if self.detectCycle(i,adj,visited):
                    return True
        
        return False
    



















    #DFS
    def detectCycleDFS(self,src,parent,adj,visited):
        visited[src]=1

        for ch in adj[src]:
            if visited[ch]==0:
                if self.detectCycleDFS(ch,src,adj,visited):
                    return True
            else:
                if ch != parent:
                    return True
        
        return False



    # TC:- O(V+2E)
    # SC:- O(V) + O(V) stack space and visited, worst case no adjacent nodes outer for loop runs n times - imagine graph with 4 nodes in first comp, 2 in second ,3 in third so outer will be called 3 times which will make sure all 9 are visited
    def isCycle(self, V,E, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u= edge[0]
            v= edge[1]
            adj[u].append(v)
            adj[v].append(u)

        visited = [0]*V

        for i in range(0,V):
            if visited[i]==0:
                if self.detectCycleDFS(i,-1,adj,visited):
                    return True
        
        return False
    
    
s1 = Solution()
V = 4
E = 4,
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
print(s1.isCycle(V,E,edges))

    


