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

            
    # Tc:- O(N *  LOG(M)) - as we are not sure if target is in row, it maybe or maybe not unlike search in 2d matrix part 1.
    # SC:- O(1)
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])

        for i in range(0,n):
            row = matrix[i]
            if target>= row[0] and target<=row[-1]:
                if self.BinarySearch(row,m, target)==True:
                    return True

        return False
    
    
    # TC:- O(N + M)
    # SC:- O(1)
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])

        i=0
        j=m-1

        while i<n and j>=0:
            if matrix[i][j]== target:
                return True
            
            elif target > matrix[i][j]:
                i+=1
            
            else:
                j-=1
        
        return False
    

 
            






s1 = Solution()
matrix = [[1],[3]]
target = 3
print(s1.searchMatrix(matrix, target))

    




