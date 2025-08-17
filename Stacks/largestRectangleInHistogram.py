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
    # TC:- O(N* N)
    # SC:- O(1)
    def largestRectangleArea(self, heights):
        ans=0
        n=len(heights)

        for i in range(0,n):
            #next smaller on right
            r=n
            for j in range(i+1,n):
                if heights[j]<heights[i]:
                    r=j
                    break
            
            l=-1
            #previous smaller on right
            for j in range(i-1,-1,-1):
                if heights[j]<heights[i]:
                    l=j
                    break
                
            
            largest = (r-l-1)*heights[i]
            
            ans = max(ans, largest)

        return ans
    
    # can also pre compute NSE and PSE but the TC WILL BE O(2N) * 2 + o(N) for main function loop as well as other stack spaces
 

s1 = Solution()
heights =[5,4,1,2]
print(s1.largestRectangleArea(heights))

    


