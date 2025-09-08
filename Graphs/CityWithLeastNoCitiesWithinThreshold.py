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



class Solution:
    # TC:- O(N^3) + O( N *M), can also be done using Dijkstras for each of the node O(V * (ELOGV))
    # SC:- O(N * M)
    def findTheCity(self, n, edges, distanceThreshold):
        dist = [[float('inf') for j in range(n)] for i in range(n)]

        for i in range(0,n):
            dist[i][i] =0
        

        for edge in edges:
            u=edge[0]
            v=edge[1]
            wt = edge[2]

            dist [u][v] = wt
            dist [v][u] = wt

        for via in range(0,n):
            for i in range(0,n):
                for j in range(0,n):
                    viaPath = dist[i][via] + dist[via][j]
                    dist[i][j] = min(dist[i][j], viaPath)

        ans= -1
        mini = float('inf')
        
        for i in range(0,n):
            count=0
            for j in range(0,n):
                if i!=j and dist[i][j]<=distanceThreshold:
                    count+=1
            
            if count<=mini:
                ans = i
                mini = count
        
        return ans
            
            


    
        
        

        
        


s1 = Solution() 
n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2
print(s1.findTheCity(n,edges,distanceThreshold))

    


