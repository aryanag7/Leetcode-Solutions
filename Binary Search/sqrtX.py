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
    # TC:-O(√x)
    # SC:- O(1)
    def mySqrt(self, x):
        ans=0
        for i in range(1,x//2+2):
            if i*i <= x:
                ans=i
            else:
                break
        
        return ans
    
    
    # TC: O(LOGN)
    # SC:- O(1)
    #can also return high as low will move towards the non answer part and will point to the first non answer and high will move towards the answer part and will point to the last answer
    def mySqrt(self, x):
        low=1
        high=x
        ans=0

        while low<=high:
            mid = low + (high-low)//2

            if mid * mid <= x:  #if mid overflow divide by mid on both sides
                ans=mid
                low=mid+1
            else:
                high=mid-1
            
        return ans


        
            

    
s1 = Solution()
x=36
print(s1.mySqrt(x))

    


