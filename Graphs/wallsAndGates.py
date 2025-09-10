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
    # TC:- O(N * M * 4)
    # SC:- O(N* M) VISITED + O(N*M) ANS GRID SHOULD NOT SOLVE ON INPUT DIRECTLY + O(N*M) QUEUE
    def wallsAndGates(self, rooms):
        n=len(rooms)
        m=len(rooms[0])

        ansGrid = [ row[:] for row in rooms]
        visited = [[0 for j in range(m)] for i in range(n)]

        queue=[]
        for i in range(0,n):
            for j in range(0,m):
                if rooms[i][j]==0:
                    queue.append((0,(i,j)))
                    visited[i][j]=1

        
        while len(queue)>0:
            steps, (i,j) = queue.pop(0)

            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            for d in directions:
                new_i = i+d[0]
                new_j = j+d[1]

                if new_i>=0 and new_i<n and new_j>=0 and new_j<m and rooms[new_i][new_j]!=-1 and visited[new_i][new_j]==0:
                    queue.append((steps+1, (new_i,new_j)))
                    visited[new_i][new_j]=1
                    ansGrid[new_i][new_j] = steps+1
        
        return ansGrid
    


        
        

s1 = Solution() 
# rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
rooms = [[-1]]
print(s1.wallsAndGates(rooms))

    


