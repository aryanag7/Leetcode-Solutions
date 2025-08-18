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
    # TC:- O(N * N)
    # SC:- O(1) if excluded ans array
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        ans=[0]*n

        for i in range(0,n):
            flag=False
            for j in range(i+1,n):
                if temperatures[j]>temperatures[i]:
                    flag=True
                    break
         
            if flag:
                ans[i]=(j-i)
        
        return ans
    

    # TC:- O(N +  N)
    # SC:- O(N) if excluded ans array
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        ans=[0]*n
        stack=[]

        for i in range(n-1,-1,-1):
            while stack and temperatures[i]>=temperatures[stack[-1]]:
                stack.pop()
            
            if stack:
                ans[i]= stack[-1] - i
            
            stack.append(i)
        
        return ans
            



    
    

 

s1 = Solution()
temperatures = [30,60,90]
print(s1.dailyTemperatures(temperatures))

    


