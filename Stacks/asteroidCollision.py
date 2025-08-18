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
    # TC:- O(N + N)
    # SC:- O(N)
    def asteroidCollision(self, asteroids):
        stack=[]

        n=len(asteroids)
        for i in range(0,n):
            if asteroids[i]>0:
                stack.append(asteroids[i])
                continue

            while stack and stack[-1]>0 and stack[-1]< abs(asteroids[i]):
                stack.pop()
            
            if stack and stack[-1]==abs(asteroids[i]):
                stack.pop()
            
            elif not(stack) or stack[-1]<0:
                stack.append(asteroids[i])

        
        return stack


    

 

s1 = Solution()
asteroids = [8,-8]
print(s1.asteroidCollision(asteroids))

    


