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
    # TC: O(N * M * 4)
    # SC:- O(1)
    def findPeakGrid(self, mat):
        n=len(mat)
        m=len(mat[0])

        for i in range(0,n):
            for j in range(0,m):
                    curr = mat[i][j]

                    above = mat[i-1][j] if i>0 else -1
                    is_above = curr > above

                    below = mat[i+1][j] if i<n-1 else -1
                    is_below = curr > below

                    left = mat[i][j-1] if j>0 else -1
                    is_left = curr > left

                    
                    right = mat[i][j+1] if j<m-1 else -1
                    is_right = curr > right

                    if is_above and is_below and is_left and is_right:
                        return [i,j]


    # TC: O(N * M)
    # SC:- O(1)              
    def findPeakGrid(self, mat):
        n=len(mat)
        m=len(mat[0])

        maxi = -1
        maxi_index = [-1,-1]

        for i in range(0,n):
            for j in range(0,m):
                if mat[i][j]> maxi:
                    maxi = mat[i][j]
                    maxi_index = [i,j]
    
        return maxi_index
    


    def findMax(self,mat,n,m,mid):
        maxi = mat[0][mid]
        maxi_row = 0

        for i in range(1,n):
            if mat[i][mid]> maxi:
                maxi = mat[i][mid]
                maxi_row=i
        
        return maxi_row
        

    # TC:- O(LOG(M) * N)
    # SC:- O(1)
    def findPeakGrid(self, mat):
        n=len(mat)
        m=len(mat[0])

        low=0
        high = m-1

        while low<=high:
            mid = low + (high -low)//2

            row = self.findMax(mat,n,m,mid)

            left =  mat[row][mid-1] if mid-1>=0 else -1
            right = mat[row][mid+1] if mid+1 < m else -1

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row,mid]
            
            elif left > mat[row][mid]:
                high = mid-1

            elif right > mat[row][mid]:
                low = mid+1
                




        

    
s1 = Solution()
mat = [[10,50,40,30,20],[1,500,2,3,4]]
print(s1.findPeakGrid(mat))

    


