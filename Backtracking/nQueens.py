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
    def safeToPlaceQueen(self,n,row,col,mat):
        i=row
        j=col

        while i>=0 and j>=0:
            if mat[i][j]=="Q":
                return False
            
            i-=1
            j-=1


        i=row
        j=col

        while j>=0:
            if mat[i][j]=="Q":
                return False
            j-=1

        i=row
        j=col

        while i<n and j>=0:
            if mat[i][j]=="Q":
                return False
            
            i+=1
            j-=1
        
        return True
          

    def solveNQueensHelper(self,n,col,mat,ans):
        if col==n:
            temp=[]
            for i in range(n):
                s=""
                for j in range(n):
                    s+=mat[i][j]

                temp.append(s)

            ans.append(temp)
            return
            
        
        for row in range(0,n):
            if self.safeToPlaceQueen(n,row,col,mat):
                mat[row][col]="Q"
                self.solveNQueensHelper(n,col+1,mat,ans)
                mat[row][col]="."

                
    def solveNQueens(self, n):
        mat=[["." for j in range(n)] for i in range(n)]
        ans=[]
        self.solveNQueensHelper(n,0,mat,ans)
        return ans
        


s1 = Solution()
n = 4
print(s1.solveNQueens(n))

    


