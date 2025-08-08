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
     # TC:- O(N^2)
     # SC:- O(1)
     # def maxArea(self, height):
     #      ans=0

     #      n=len(height)
     #      for i in range(0,n):
     #           for j in range(i+1,n):
     #                totalWater = min(height[i],height[j]) *  (j-i)
     #                ans=max(ans,totalWater)
          
     #      return ans
     
     
     
     # TC:- O(N)
     # SC:- O(1)
     def maxArea(self, height):
          ans=0
          i=0
          n=len(height)
          j=n-1

          while i<j:
               totalWater = min(height[i],height[j]) *  (j-i)
               ans=max(ans,totalWater)

               if height[i]<=height[j]:
                    i+=1
               else:
                    j-=1
          
          return ans




s1 = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(s1.maxArea(height))
    

