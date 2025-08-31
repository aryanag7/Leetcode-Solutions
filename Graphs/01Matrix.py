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
    # TC:- O(N * M * 4)
    # SC:- O(N* M) + O(N * M) 
    def updateMatrix(self, mat):
        n=len(mat)
        m=len(mat[0])

        ansMatrix = [row[:] for row in mat]

        visited=[[0 for j in range(m)] for i in range(n)]

        queue=[]
        for i in range(0,n):
            for j in range(0,m):
                if mat[i][j]==0:
                    queue.append(((i,j),0))
                    visited[i][j]=1
        
        while len(queue)>0:
            (i,j), level = queue.pop(0)

            directions = [(-1,0),(0,-1),(1,0),(0,1)]

            for d in directions:
                new_i = i+d[0]
                new_j = j+d[1]

                if new_i>=0 and new_i<n and new_j>=0 and new_j<m and  mat[new_i][new_j]==1 and visited[new_i][new_j]==0:
                    queue.append(((new_i,new_j),level+1))
                    ansMatrix[new_i][new_j] = level+1
                    visited[new_i][new_j]=1
        

        return ansMatrix
        

    
s1 = Solution()
mat = [[1,1,1],[1,1,1],[0,1,0]]
print(s1.updateMatrix(mat))

    


