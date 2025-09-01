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
    def DFS_traversal(self,src, V, adj, visited, pathVisited):
        visited[src]=1
        pathVisited[src]=1

        for ch in adj[src]:
            if visited[ch]==0:
                if self.DFS_traversal(ch, V, adj, visited, pathVisited):
                    return True
            else:
                if pathVisited[ch]==1:
                    return True
        
        pathVisited[src]=0
        return False
     
     

    # TC:- O(V +E)
    # SC:- O(V) + O(V)
    #CAN ALSO MARK A NODE AS 1 FOR VISITED AND 2 FOR PATH VISITED IN THE SAME VISITED ARRAY INSTEAD OF A NEW ONE
    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)]

        for edge in edges:
            u=edge[0]
            v=edge[1]

            adj[u].append(v)

        visited = [0]*V
        pathVisited = [0]*V

        for i in range(0,V):
            if visited[i]==0:
                if self.DFS_traversal(i, V, adj, visited, pathVisited):
                    return True
        
        return False


          







    
s1 = Solution() 
V = 4
edges= [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]
print(s1.isCycle(V, edges))

    


