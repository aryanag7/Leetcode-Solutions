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



#Complexity is O(4 * alpha) ~alpha close to 1 so constant time
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
        


#you can have bi-directional edge in edges or just 1 doesn't matter as the second will be discarded by DSU
# edges [5,1,2], [5,2,1] assume wt to be 5 and u=1 and v=2, when we'll union [5,1,2] DSU will add it and when we are on [5.2.1] 2 and 1 will be part of same MST
class Solution:
    # TC:- M EDGES, MLOG(M) FOR SORTING AND O(M * 4 alpha)
    def kruskalsMST(self, V, E, edges):
        dsu = DisjointSet(V)

        edges.sort(key = lambda x:x[2])

        s=0
        ans=[]
        for edge in edges:  
            u = edge[0]
            v = edge[1]
            wt = edge[2]

            if dsu.findUltimateParent(u) != dsu.findUltimateParent(v):
                s+=wt
                ans.append((u,v))
                dsu.UnionBySize(u,v)
        
        return s,ans



    
s1 = Solution()
V = 3
E = 3
edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
print(s1.kruskalsMST(V,E,edges))

    


