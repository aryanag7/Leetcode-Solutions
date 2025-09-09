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
    def Dfs_traversal(self,i,j,n,m,heights, cellSet,visited):
        cellSet.add((i,j))
        visited[i][j]=1

        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        for d in directions:
            new_i = i+d[0]
            new_j = j+d[1]

            if new_i>=0 and new_i<n and new_j>=0 and new_j<m and visited[new_i][new_j]==0 and heights[new_i][new_j]>= heights[i][j]:
                self.Dfs_traversal(new_i,new_j,n,m,heights, cellSet,visited)

    

    # TC:- DFS for each pacific and atlantic O(N*M*4) + O(N*M*4) IF ALL CELLS VALID
    # SC:- O(N*M) + O(N*M) FOR VISITED , O(N*M) if all cells in both sets, stack space O(N*M) if all cells valid
    def pacificAtlantic(self, heights):
        n= len(heights)
        m=len(heights[0])

        pacific_set = set()
        pacific_visited = [[0 for _ in range(m)] for _ in range(n)]



        #cells borderiing pacific ocean - first row
        for j in range(0,m):
            if pacific_visited[0][j]==0:
                self.Dfs_traversal(0,j,n,m,heights, pacific_set,pacific_visited)
        

        #cells borderiing pacific ocean - first col
        for i in range(0,n):
            if pacific_visited[i][0]==0:
                self.Dfs_traversal(i,0,n,m,heights, pacific_set,pacific_visited)
        


        atlantic_set = set()
        atlantic_visited = [[0 for _ in range(m)] for _ in range(n)]



        #cells borderiing atlantic ocean - last row
        for j in range(0,m):
            if atlantic_visited[n-1][j]==0:
                self.Dfs_traversal(n-1,j,n,m,heights, atlantic_set,atlantic_visited)
        

        #cells borderiing pacific ocean - last col
        for i in range(0,n):
            if atlantic_visited[i][m-1]==0:
                self.Dfs_traversal(i,m-1,n,m,heights, atlantic_set,atlantic_visited)
        
        return [ list(t) for t in  pacific_set & atlantic_set]
        
        



        
        

        
        


s1 = Solution() 
heights = [[1]]
print(s1.pacificAtlantic(heights))

    


