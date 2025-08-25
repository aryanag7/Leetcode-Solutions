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
    # TC:- O(N* M)
    # SC:- O(1)
    def rowAndMaximumOnes(self, mat):
        n=len(mat)
        m=len(mat[0])
        ans=[-1,-1]

        for i in range(0,n):
            ones = 0
            for j in range(0,m):
                if mat[i][j]==1:
                    ones+=1

            if ones>ans[1]:
                ans[1]= ones
                ans[0]=i
        
        return ans
    

    # TC:- O(N * (M LOG M + LOG(M)))) above is the better one 
    # SC:- O(1)
    def rowAndMaximumOnes(self, mat):
        n=len(mat)
        m=len(mat[0])
        ans=[0,0]

        for i in range(0,n):
            row = mat[i]
            row.sort()
            num_ones = bisect.bisect_left(row,1)
            if num_ones!=m and m-num_ones > ans[1]:
                ans[1] = m-num_ones
                ans[0]=i

        return ans 


    
    #IF THE INPUT ROWS ARE ALREADY SORTED, CAN FURTHER OPTIMIZE TO O(N+M)
    def rowAndMaximumOnes(self, mat):
        n=len(mat)
        m=len(mat[0])

        i=0
        j=m-1

        ans=-1

        while i<n and j>=0:
            if mat[i][j]==1:
                ans = max(ans, i)
                j-=1
            else:
                i+=1
        
        return ans


            
        

            






s1 = Solution()
mat = [[1,1,1,1,1,],[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0],[0,1,1,1,1]]
print(s1.rowAndMaximumOnes(mat))

    




