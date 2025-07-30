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
    #TC:- O(3^N ) EACH digits has 3 choices, so for n digits 3x3x3...n
    #SC:- O(N)
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        letterMap = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"prqs",8:"tuv",9:"wxyz"}
        ans=[]

        def letterComboHelper(digits,ind,letterMap,s):
            if ind==len(digits):
                ans.append(s)
                return



            key = int(digits[ind])
            for letter in letterMap[key]:
                letterComboHelper(digits,ind+1, letterMap, s+letter)




        letterComboHelper(digits,0,letterMap,s="")

        return ans
        
    


s1 = Solution()
digits = "23"
print(s1.letterCombinations(digits))

    


