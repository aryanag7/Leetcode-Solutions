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

    # TC:- O(3N)
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
          

    # TC:- O(1) - Using Hashing     
    def safeToPlaceQueen(self,n,row,col,mat,rowMap,downDiagonal,upDiagonal):
        if upDiagonal[(n-1)+(row-col)]:
            return False

        if rowMap[row]:
            return False

        if downDiagonal[row+col]:
            return False

        return True
        

    def solveNQueensHelper(self,n,col,mat,ans,rowMap,downDiagonal,upDiagonal):
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
            if self.safeToPlaceQueen(n,row,col,mat,rowMap,downDiagonal,upDiagonal):
                mat[row][col]="Q"
                rowMap[row]=True
                downDiagonal[row+col]= True
                upDiagonal[(n-1)+(row-col)] = True

                self.solveNQueensHelper(n,col+1,mat,ans,rowMap,downDiagonal,upDiagonal)

                mat[row][col]="."
                rowMap[row]=False
                downDiagonal[row+col]= False
                upDiagonal[(n-1)+(row-col)] = False


    #TC:- O(N^N)
    def solveNQueens(self, n):
        mat=[["." for j in range(n)] for i in range(n)]
        rowMap= [False]*n
        downDiagonal = [False]*(2*n-1)
        upDiagonal= [False]*(2*n-1)
        ans=[]
        self.solveNQueensHelper(n,0,mat,ans,rowMap,downDiagonal,upDiagonal)
        return ans
        


s1 = Solution()
n = 4
print(s1.solveNQueens(n))

    


