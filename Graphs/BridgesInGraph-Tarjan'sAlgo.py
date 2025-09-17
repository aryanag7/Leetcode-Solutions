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
    time = 1

    def dfs(self,node, parent , visited, step, low, adj,ans):
        visited[node]=1

        step[node] , low[node] = Solution.time, Solution.time

        Solution.time+=1

        for ch in adj[node]:
            if ch == parent:
                continue

            elif visited[ch]==0:
                self.dfs(ch, node , visited, step, low, adj, ans)
                low[node] = min(low[node], low[ch])

                if low[ch] > step[node]:
                    ans.append([node,ch])

            else:
                low[node] = min(low[node], low[ch])



    # TC:- O(V+2E)
    # SC:- O(V+2E) +  O(3*V)
    def criticalConnections(self, n: int, connections):
        adj = [[] for _ in range(n)]

        for connection in connections:
            u = connection[0]
            v = connection[1]
            
            adj[u].append(v)
            adj[v].append(u)
        
        step = [0] * n
        low = [0] * n
        visited = [0] * n
        ans = []

        self.dfs(0, -1 , visited, step, low, adj,ans)

        return ans





         

        




s1 = Solution() 
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print(s1.criticalConnections(n,connections))

    


