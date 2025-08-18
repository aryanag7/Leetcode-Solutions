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
    # TC:- O(N * LOGN)
    # SC:- O(N)
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        
        times=[]
        for car in cars:
            distance = target - car[0]
            times.append((distance/car[1]))
        
        
        
        fleets=0
        maxi=0

        for t in times:
            if t>maxi:
                fleets+=1
                maxi=t
        
        return fleets
    
    #REDUCED PASS WITH ALONG WITH STACK
    
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        
        stack=[]
        for car in cars[::-1]:
            time = (target-car[0]) / car[1]
            while stack and time>=stack[-1]:
                stack.pop()
        
            stack.append(time)
        
        return len(stack)

        
    

 

s1 = Solution()
target = 12
position =  [10,8,0,5,3]
speed = [2,4,1,1,3]
print(s1.carFleet(target,position,speed))

    


