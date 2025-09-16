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
    def dfs_traverse(self,i,j,n,m,matrix,visited):
        visited[i][j] = 1

        #stone on same row
        for k in range(0,m):
            if matrix[i][k]==1 and visited[i][k]==0:
                self.dfs_traverse(i,k,n,m,matrix,visited)
        

        for k in range(0,n):
            if matrix[k][j]==1 and visited[k][j]==0:
                self.dfs_traverse(k,j,n,m,matrix,visited)



    # TC:- if all cells are stones then n*m func calls and each call is o(r+c) row + col, 
    # SC:- O(N * M) + O(N *M)
    #COULD be inefficient because storing the whole matrix with many unused cells, instead store all the stones only in row and col maps
    def removeStones(self, stones):
        row = max(stone[0] for stone in stones)
        col = max(stone[1] for stone in stones)
        
        matrix = [[0 for j in range(col+1)] for i in range(row+1)]

        for stone in stones:
            i = stone[0]
            j = stone[1]
            matrix[i][j]=1
        
        visited = [[0 for j in range(col+1)] for i in range(row+1)]

        components = 0
        for i in range(0,row+1):
            for j in range(0,col+1):
                if matrix[i][j]==1 and visited[i][j]==0:
                    self.dfs_traverse(i,j,row+1,col+1,matrix,visited)
                    components+=1
        

        
        return len(stones) - components
    






    #instead of storing the full matrix with many unused cells with no stones we can store the 

    # def dfs_traverse(self, r, c, row_map, col_map, visited):
    #     visited.add((r, c))
        
    #     # stones in the same row
    #     for nr, nc in row_map[r]:
    #         if (nr, nc) not in visited:
    #             self.dfs_traverse(nr, nc, row_map, col_map, visited)
        
    #     # stones in the same column
    #     for nr, nc in col_map[c]:
    #         if (nr, nc) not in visited:
    #             self.dfs_traverse(nr, nc, row_map, col_map, visited)

    # def removeStones(self, stones: List[List[int]]) -> int:
    #     row_map = defaultdict(list)
    #     col_map = defaultdict(list)
        
    #     for r, c in stones:
    #         row_map[r].append((r, c))
    #         col_map[c].append((r, c))
        
    #     visited = set()
    #     components = 0
        
    #     for r, c in stones:
    #         if (r, c) not in visited:
    #             self.dfs_traverse(r, c, row_map, col_map, visited)
    #             components += 1
        
    #     return len(stones) - components





s1 = Solution() 
stones = [[0,0]]
print(s1.removeStones(stones))

    


