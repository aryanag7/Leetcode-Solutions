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
    def DFS_traversal(self,src,adj,V,visited):
        visited[src]=1

        for ch in adj[src]:
            if visited[ch]==0:
                self.DFS_traversal(ch,adj,V,visited)

    # TC:- O(V+2E) - overall traversing graph
    # SC:- O(V) + O(V) + O(V) for visited and adj list and stack space
    def findCircleNum(self, isConnected):
        V=len(isConnected)
        adj = [[] for _ in range(V)]

        for i in range(V):
            for j in range(V):
                if i!=j and isConnected[i][j]==1:
                    adj[i].append(j)
        
        
        provincesCount =0

        visited = [0]*(V)

        for i in range(0,V):
            if visited[i]==0:
                self.DFS_traversal(i,adj,V,visited)
                provincesCount+=1

        return provincesCount




        

        
        


    
s1 = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(s1.findCircleNum(isConnected))

    


