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
    # SC:- O(3) for map and O(N) for stack
    def isValid(self, s):
        bracketMap = {")":"(", "]":"[", "}":"{"}
        stack=[]

        n=len(s)
        for i in range(0,n):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                stack.append(s[i])
            else:
                if len(stack)>0 and stack[-1]== bracketMap[s[i]]:
                    stack.pop()
                else:
                    return False
                
        return len(stack)==0



            
 


s1 = Solution()
s = "()[]{}"
print(s1.isValid(s))

    


