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
    # TC:- O(N)
    # SC:- O(1)
    def findKthPositive(self, arr, k):
        n=len(arr)
        prev_missing = 0
        for i in range(0,n):
            actual = i+1
            missing = arr[i] - actual

            if missing>= k:
                curr_missing = k - prev_missing 
                return arr[i-1]+curr_missing if i>0 else curr_missing

            prev_missing = missing
        
        return arr[-1] + (k - prev_missing)
    


    # TC:- O(LOG(N))
    # SC:- O(1)
    def findKthPositive(self, arr, k):
        low=0
        n=len(arr)
        high = n-1

        while low<= high:
            mid = low + (high -low)//2

            missing = arr[mid] - (mid+1)

            if missing<k:
                ans = mid
                low = mid+1
            
            else:
                high = mid-1
        
        
        missing = arr[ans] - (ans+1)
        return arr[ans] + (k - missing)
        

    
            
s1 = Solution()
arr = [2,3,4,7,11]
k = 3
print(s1.findKthPositive(arr,k))

    




