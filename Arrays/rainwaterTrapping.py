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
    # def trap(self, height):
    #     ans=0
    #     n=len(height)
    #     for i in range(1,n-1):
    #         leftMax = -1
    #         rightMax = -1
            
    #         j=i-1
    #         while j>=0:
    #             leftMax = max(leftMax, height[j])
    #             j-=1
            
    #         k=i+1
    #         while k<n:
    #             rightMax = max(rightMax, height[k])
    #             k+=1


    #         if leftMax > height[i] and rightMax > height[i]:
    #             ans+=min(leftMax,rightMax ) - height[i]
            
        
    #     return ans
    
    # Can be done using prefixmax and suffix max, can also skip creating prefixmax as iterating from left, can keep leftmax in a variable


#
    # TC:- O(N)
    # SC:- O(1)
    def trap(self, height):
        i=0
        n=len(height)
        j=n-1
        ans=0

        leftMax=0
        rightMax=0

        while i<j:
            leftMax = max(leftMax,height[i])
            rightMax = max(rightMax,height[j])

            if leftMax<=rightMax:
                ans+= (leftMax-height[i])
                i+=1

            else:
                ans+= (rightMax-height[j])
                j-=1
            
        return ans



s1 = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s1.trap(height))
    

