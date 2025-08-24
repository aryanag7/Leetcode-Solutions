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
    # TC:- O( SUM(ARR)-MAX(ARR)+1 * N)
    # SC:- O(1)
    def findPages(self, arr, k):
        n=len(arr)
        if k > n:
            return -1
        
        total_pages = 0
        for i in arr:
            total_pages+=i

        for max_pages in range(max(arr), total_pages+1 ):
            students_allocated = 1
            s = 0

            for i in range(0,n):
                s+= arr[i]

                if s > max_pages:
                    students_allocated+=1
                    s=arr[i]
        
            if students_allocated<=k:
                return max_pages
            
    def isPossible(self,max_pages, arr, k):
        n=len(arr)
        students_allocated = 1
        s = 0

        for i in range(0,n):
            s+= arr[i]

            if s > max_pages:
                students_allocated+=1
                s=arr[i]
    
        return students_allocated<=k
            

    # TC:- O( LOG(SUM(ARR)-MAX(ARR)+1) * N)
    # SC:- O(1)     
    def findPages(self, arr, k):
        n=len(arr)
        if k > n:
            return -1
        
        total_pages = 0
        for i in arr:
            total_pages+=i
        
        low = max(arr)
        high = total_pages

        ans=-1

        while low<= high:
            mid = low + (high-low)//2

            if self.isPossible(mid, arr, k):
                ans = mid
                high = mid-1
            
            else:
                low= mid+1
        
        return ans
    

s1 = Solution()
arr = [12, 34, 67, 90]
k = 2
print(s1.findPages(arr,k))

    




