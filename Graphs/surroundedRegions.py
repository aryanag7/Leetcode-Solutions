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
    def DFS_traversal(self,i,j,board, visited,n,m):
        visited[i][j]=1

        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        for d in directions:
            new_i = i +d[0]
            new_j = j +d[1]

            if new_i>=0 and new_i<n and new_j>=0 and new_j<m and visited[new_i][new_j]==0 and board[new_i][new_j]=="O":
                self.DFS_traversal(self,new_i,new_j,board, visited,n,m)


    # TC:- O(N * m * 4) + O(N) for loops
    # SC:- O(N*M) visited +  O(N*m) for answer if it wouldn't have told to modify
    def solve(self, board):
        n=len(board)
        m=len(board[0])

        visited = [[0 for _ in range(m)] for _ in range(n)]

        #start DFS from first and last row
        for j in range(m):
            if board[0][j]=="O" and visited[0][j]==0:
                self.DFS_traversal(0,j,board, visited,n,m)

            
            if board[n-1][j]=="O" and visited[n-1][j]==0:
                self.DFS_traversal(n-1,j,board, visited,n,m)
        

        
        #start DFS from first and last column
        for i in range(0,n):
            if board[i][0]=="O" and visited[i][0]==0:
                self.DFS_traversal(i,0,board, visited,n,m)

            if board[i][m-1]=="O" and visited[i][m-1]==0:
                self.DFS_traversal(i,m-1,board, visited,n,m)


        for i in range(n):
            for j in range(m):
                if visited[i][j]==0 and board[i][j]=="O":
                    board[i][j]="X"
        
        return board



    
s1 = Solution() 
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(s1.solve(board))

    


