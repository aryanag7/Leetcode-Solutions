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
    # TC:- O( N * M * 4 * 4 alpha)
    # SC:- O(N * M) DSU, set will have atmost 4 ultimate parent for a current cell
    def largestIsland(self, grid):
        n = len(grid)
        m = len(grid[0])

        dsu = DisjointSet(n*m)

        for i in range(0,n):
            for j in range(0,m):

                if grid[i][j]==0:
                    continue

                curr_cell = (i * m) + j

                directions = [(-1,0),(0,-1),(1,0),(0,1)]

                for d in directions:
                    new_i = i +d[0]
                    new_j = j +d[1]

                    if new_i>=0 and new_i<n and new_j>=0 and new_j<m and grid[new_i][new_j]==1:
                        
                        adj_cell = (new_i * m) + new_j

                        if dsu.findUltimateParent(curr_cell) != dsu.findUltimateParent(adj_cell):
                            dsu.UnionBySize(curr_cell, adj_cell)
                     

        print(dsu.size)
        
        
        ans= 0

        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j]==0:
                    directions = [(-1,0),(0,-1),(1,0),(0,1)]

                    unique_parent = set()
                    for d in directions:
                        new_i = i +d[0]
                        new_j = j +d[1]
                        
                        if new_i>=0 and new_i<n and new_j>=0 and new_j<m and grid[new_i][new_j]==1:
                            
                            adj_cell = (new_i * m) + new_j
                            parent = dsu.findUltimateParent(adj_cell)
                            unique_parent.add(parent)
                    
                    area = 0
                    for p in unique_parent:
                        area += dsu.size[p]
                    if i==1 and j==2:
                        print(unique_parent)

                    ans = max(ans , area+1)

                    print(i,j,ans)
                
        for i in range(0, n*m):
            ans = max(ans, dsu.size[i])
        
        return ans


                                

                            






                        






s1 = Solution() 
grid =[[1,1],[1,0]]
print(s1.largestIsland(grid))

    


