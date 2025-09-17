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

    def dfs(self,node, parent , visited, step, low, adj, mark):
        visited[node]=1

        step[node] , low[node] = Solution.time, Solution.time

        Solution.time+=1

        childs = 0

        for ch in adj[node]:
            if ch == parent:
                continue

            elif visited[ch]==0:
                self.dfs(ch, node , visited, step, low, adj, mark)

                low[node] = min(low[node], low[ch])

                if low[ch] >= step[node] and parent!=-1:
                    mark[node]=1
                
                childs+=1
                   

            else:
                low[node] = min(low[node], step[ch])
        
        if parent == -1 and childs>1:
            mark[node]=1



    # TC:- O(V+2E)
    # SC:- O(V+2E) +  O(3*V)
    def articulationPoints(self, V, adj):

        step = [0] * n
        low = [0] * n
        visited = [0] * n
        mark = [0] * n
        
        for i in range(0,V):
            if visited[i]==0:
                self.dfs(i, -1 , visited, step, low, adj, mark)
        
        ans=[]
        for i in range(0,V):
            if mark[i]==1:
                ans.append(i)
        

        return ans if len(ans)>0 else -1

        

        




         

        




s1 = Solution() 
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print(s1.articulationPoints(n,connections))

    


