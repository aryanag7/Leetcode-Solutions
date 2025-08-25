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
    # tc:- O(N * M)
    # SC:- O(1)
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])

        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j]== target:
                    return True
        return False
    




    def BinarySearch(self,row,m, target):
        low=0
        high = m-1
        while low<=high:
            mid = low+ (high-low)//2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid+1
            
            else:
                high = mid-1
        
        return False

            
    # Tc:- O(N +  LOG(M)) - AS Binary search happens only once for a row, not for all rows
    # SC:- O(1)
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])

        for i in range(0,n):
            row = matrix[i]
            if self.BinarySearch(row,m, target)==True:
                return True

        return False
    

    # same as above almost

    # TC:- O(N + M) - ROWS ALREADY SORTED
    # SC:- O(1)
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])

        i=0
        j= m-1

        while i<n and j>=0:
            if matrix[i][j]==target:
                return True

            elif target > matrix[i][j]:
                i+=1
            
            else:
                j-=1
        
        return False


    # TC:- OLOG(N* M)) - ROWS ALREADY SORTED
    # SC:- O(1)
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])

        low=0
        high= n*m -1

        while low<=high:
            mid = low + (high-low)//2

            i= mid//m
            j= mid%m

            if matrix[i][j]== target:
                return True

            elif matrix[i][j] > target:
                high = mid-1
            
            else:
                low = mid +1 

        return False


            






s1 = Solution()
matrix = [[1],[3]]
target = 3
print(s1.searchMatrix(matrix, target))

    




