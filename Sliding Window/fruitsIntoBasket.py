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
      # TC:- O(N*N)
      # SC:- O(N) in this case you store 3 elements at max
      # def totalFruit(self, fruits):
      #       ans=0
      #       n=len(fruits)

      #       for i in range(0,n):
      #             seen=set()
      #             for j in range(i,n):
      #                   seen.add(fruits[j])
      #                   if len(seen)>2:
      #                         break

      #                   ans= max(ans, j-i+1)

      #       return ans
      

      
      
      # TC:- O(N+N)
      # SC:- O(3) at most 3 elements then we start to remove  
      def totalFruit(self, fruits):
            ans=0
            l=0
            r=0
            n=len(fruits)
            d = defaultdict(int)

            while r<n:
                  d[fruits[r]]+=1


                  # converting in valid window to valid one
                  while len(d)>2:
                        d[fruits[l]]-=1
                        if d[fruits[l]]==0:
                              d.pop(fruits[l])
                        l+=1


                  ans=max(ans, r-l+1)
                  r+=1

            return ans
      
            
      # TC:- O(N)
      # SC:- O(3) at most 3 elements then we start to remove  
      def totalFruit(self, fruits):
            ans=0
            l=0
            r=0
            n=len(fruits)
            d = defaultdict(int)

            while r<n: #while here window is from l to r-1
                  d[fruits[r]]+=1


                  # converting in valid window to valid one
                  if len(d)>2:
                        d[fruits[l]]-=1
                        if d[fruits[l]]==0:
                              d.pop(fruits[l])
                        l+=1


                  if len(d)<=2:
                        ans=max(ans, r-l+1)

                  r+=1

            return ans






        




            
 


s1 = Solution()
fruits = [1,2,3,2,2]
print(s1.totalFruit(fruits))

    


