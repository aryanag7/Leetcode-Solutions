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
    # TC:- O(N*M) + N*M LOGN*M (SORT)
    # SC:- O(N*M) AND O(N) SORTING SPACE IN PYTHON 
    def matrixMedian(self, grid):
        temp = []
        n=len(grid)
        m=len(grid[0])

        for i in range(0,n):
            for j in range(0,m):
                temp.append(grid[i][j])
        
        temp.sort()

        return temp[(n*m)//2]
    



    def canBeAnswer(self,num, grid, n,m):
        total =0

        for row in grid:
            total+=bisect.bisect_right(row,num)
        
        return total > (n*m)//2


    # TC:- O(LOG(MAX-MIN+1) * N*LOG(M))
    def matrixMedian(self, grid):
        n=len(grid)
        m=len(grid[0])

        mini= float('inf')
        for i in range(0,n):
            mini = min(mini, grid[i][0])

        maxi= float('-inf')
        for i in range(0,n):
            maxi = max(maxi, grid[i][m-1])
        
        low = mini
        high = maxi
        ans= -1

        while low<=high:
            mid = low + (high-low)//2

            if self.canBeAnswer(mid, grid, n,m):
                ans = mid
                high = mid-1

            else:
                low = mid +1
        
        return ans







        
            
    
s1 = Solution()
grid = [[1,1,2],[2,3,3],[1,3,4]]
print(s1.matrixMedian(grid))

    




