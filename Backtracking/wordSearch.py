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
    # TC:- (m × n) × (3^L) × (L) - L cuz of string copy
    #SC:- O(m*n) may visited each cell in every path , O(M*N) visited
    def wordExists(self,board,word,m,n,i,j,currWord,visited):
        if currWord==word:
            return True
        
        if i<0 or j<0 or i>=m or j>=n or visited[i][j]!=0:
            return False

        

        visited[i][j]=1
        currWord+= board[i][j]

        left = self.wordExists(board,word,m,n,i,j-1,currWord,visited)

        right =  self.wordExists(board,word,m,n,i,j+1,currWord,visited)

        up =  self.wordExists(board,word,m,n,i-1,j,currWord,visited)

        down = self.wordExists(board,word,m,n,i+1,j,currWord,visited)
    
        visited[i][j]=0


        return left or right or up or down
    

    # TC:- O(M * N * 3^L exponential) - 1 call cut cuz of not going from where you came (visited)
    #SC:- O(L), O(M*N) visited
    def wordExists(self,board,word,m,n,i,j,k,visited):
        if k==len(word):
            return True
        
        if i<0 or j<0 or i>=m or j>=n or visited[i][j]!=0 or board[i][j]!=word[k]:
            return False

        

        visited[i][j]=1

        left = self.wordExists(board,word,m,n,i,j-1,k+1,visited)

        right =  self.wordExists(board,word,m,n,i,j+1,k+1,visited)

        up =  self.wordExists(board,word,m,n,i-1,j,k+1,visited)

        down = self.wordExists(board,word,m,n,i+1,j,k+1,visited)
    
        visited[i][j]=0


        return left or right or up or down





    def exist(self, board, word):
        m=len(board)
        n=len(board[0])
        visited=[[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if self.wordExists(board,word,m,n,i,j,0,visited):
                    return True
        
        return False
        
    
s1 = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(s1.exist(board,word))

    


