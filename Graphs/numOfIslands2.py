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

class DisjointSet:
    def __init__(self,n):
        self.n = n
        self.rank = [0]*(n+1)

        self.parent = [0]*(n+1)
        for i in range(1,n+1):
            self.parent[i]=i
        
        self.size = [1]*(n+1)
        
    
    def findUltimateParent(self,node):
        if node == self.parent[node]:
            return node
        
        val = self.findUltimateParent(self.parent[node])

        self.parent[node] = val

        return val


    def UnionByRank(self,u,v):
        ulti_par_u = self.findUltimateParent(u)
        ulti_par_v = self.findUltimateParent(v)

        if ulti_par_u == ulti_par_v:
            return 

        if self.rank[ulti_par_u]  < self.rank[ulti_par_v]:
            self.parent[ulti_par_u] = ulti_par_v
        
        elif self.rank[ulti_par_v] < self.rank[ulti_par_u]:
            self.parent[ulti_par_v] = ulti_par_u
        
        else:
            self.parent[ulti_par_v] = ulti_par_u
            self.rank[ulti_par_u]+=1

    def UnionBySize(self,u,v):
        ulti_par_u = self.findUltimateParent(u)
        ulti_par_v = self.findUltimateParent(v)

        if self.size[ulti_par_u] < self.size[ulti_par_v]:
            self.parent[ulti_par_u]= ulti_par_v
            self.size[ulti_par_v]+= self.size[ulti_par_u]
        
        else:
            self.parent[ulti_par_v] = ulti_par_u
            self.size[ulti_par_u]+= self.size[ulti_par_v]
        
        

class Solution:
    def numIslands2(self, m, n, positions):
        visited  = [[0 for j in range(n)] for i in range(m)]

        dsu = DisjointSet(m*n)

        components = 0
        ans = []
        for pos in positions:
            i , j = pos[0], pos[1]
            if visited[i][j] == 1:
                ans.append(components)
                continue
            
            visited[i][j]=1

            cell = (i*n) + j

            components+=1

            directions = [(-1,0),(0,-1),(1,0),(0,1)]

            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]

                if new_i>=0 and new_i<m and new_j>=0 and new_j<n and visited[new_i][new_j]==1:
                    adjCell = (new_i * n) + new_j

                    if dsu.findUltimateParent(cell) != dsu.findUltimateParent(adjCell):
                        dsu.UnionBySize(cell,adjCell)
                        components-=1
            
            ans.append(components)

        return ans








        






    
s1 = Solution() 
m = 3
n = 3
positions = [[0,0],[0,1],[1,2],[2,1]]
print(s1.numIslands2(m,n, positions))

    


