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
    def twoSum(self, numbers, target):
        n=len(numbers)
        for i in range(0,n):
            for j in range(i+1,n):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]


    # TC:- O(N)
    # SC:- O(1)
    def twoSum(self, numbers, target):
        n=len(numbers)
        i=1
        j=n

        while i<j:
            s = numbers[i-1] + numbers[j-1]

            if s<target:
                i+=1
            
            elif s>target:
                j-=1
            
            else:
                return [i,j]


s1 = Solution()
numbers = [2,7,11,15]
target = 9
print(s1.twoSum(numbers,target))
    

