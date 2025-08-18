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
    # TC:- for n =3 we have 2*n = 6 chars for every char either "(" or ")" but less than that as invalid sequences are avoided.
    # so O(2 ^ (2n) )
    # O(2N)

    # Cn​= 1/N+1 * ​(2N/ N​)
    # lhs is charsCn - 6C3
    def generateParenthesis(self, n):
        ans=[]

        def backtrack(n,open,close,s):
            if open == close == n:
                ans.append(s)
                return

            if open<n:
                backtrack(n,open+1,close, s + "(") 
            
            if close<open:
                backtrack(n,open, close+1, s + ")")

        
        backtrack(n,0,0,"")
        return ans
  
    

 

s1 = Solution()
n=3
print(s1.generateParenthesis(n))

    


