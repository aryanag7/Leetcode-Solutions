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
        
        

        

# ds = DisjointSet(7)
# ds.UnionByRank(1,2)
# ds.UnionByRank(2,3)
# ds.UnionByRank(4,5)
# ds.UnionByRank(6,7)
# ds.UnionByRank(5,6)

# #check if 3 and 7 are part of same component
# if ds.findUltimateParent(3) == ds.findUltimateParent(7):
#     print("True")
# else:
#     print("False")

# ds.UnionByRank(3,7)

# #check if 3 and 7 are part of same component
# if ds.findUltimateParent(3) == ds.findUltimateParent(7):
#     print("True")
# else:
#     print("False")     

ds = DisjointSet(7)
ds.UnionBySize(1,2)
ds.UnionBySize(2,3)
ds.UnionBySize(4,5)
ds.UnionBySize(6,7)
ds.UnionBySize(5,6)

#check if 3 and 7 are part of same component
if ds.findUltimateParent(3) == ds.findUltimateParent(7):
    print("True")
else:
    print("False")

ds.UnionBySize(3,7)

#check if 3 and 7 are part of same component
if ds.findUltimateParent(3) == ds.findUltimateParent(7):
    print("True")
else:
    print("False")     




