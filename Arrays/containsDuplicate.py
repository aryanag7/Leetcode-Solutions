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
    # TC:- O(N)
    # SC:- O(N) 
    def containsDuplicate(self, nums):
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        
        return False
        
   


s1 = Solution()
nums = [1,2,3]
print(s1.containsDuplicate(nums))

    


