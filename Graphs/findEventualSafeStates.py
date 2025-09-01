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
    def DFS_traversal(self,src, V, adj, visited, pathVisited,safeNodes):
        visited[src]=1
        pathVisited[src]=1

        for ch in adj[src]:
            if visited[ch]==0:
                if self.DFS_traversal(ch, V, adj, visited, pathVisited,safeNodes):
                    return True

            else:
                if pathVisited[ch]==1:
                    return True


        
        pathVisited[src]=0
        safeNodes[src]=1
        return False


    def eventualSafeNodes(self, graph):
        V= len(graph)

        visited= [0]*V
        pathVisited = [0]*V
        safeNodes = [0]*V

        for i in range(0,V):
            if visited[i]==0:
                self.DFS_traversal(i,V, graph, visited, pathVisited, safeNodes)

        
        ans=[]
        for i in range(0,V):
            if safeNodes[i]:
                ans.append(i)
        
        return ans




          







    
s1 = Solution() 
graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(s1.eventualSafeNodes(graph))

    


