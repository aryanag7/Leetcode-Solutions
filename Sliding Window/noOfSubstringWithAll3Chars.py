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
     # SC:- O(3)
     # def numberOfSubstrings(self, s):
     #      ans=0

     #      n=len(s)
     #      for i in range(0,n):
     #           seen=set()
     #           for j in range(i,n):
     #                seen.add(s[j])

     #                if len(seen)==3:
     #                     ans+= (n-j)
     #                     break
                         
          
     #      return ans




     # TC:- O(N + N)
     # SC:- O(3)
     def numberOfSubstrings(self, s):
          l=0
          r=0

          ans=0
          n=len(s)
          d=defaultdict(int)

          while r<n:
               d[s[r]]+=1
               
          
               # here we start from l=0 as starting char then expand and find a valid window, count substrings for it then shrink from left to find a new l as starting char where the window from l to r is valid and count substrings  for that.
               while len(d)==3:

                    ans+= (n-r)

                    d[s[l]]-=1
                    if d[s[l]]==0:
                         d.pop(s[l])
                    l+=1

               #this is where len(d)<3 , we keep moving
               
               r+=1
          
          return ans




            


     
               


        

    
s1 = Solution()
s ="bbacba"
print(s1.numberOfSubstrings(s))

    


