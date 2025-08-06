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
# Just using a separator (like '#') won't work if strings themselves contain that separator.
# Just using a number prefix without a separator won't work because we can't tell where the number ends if it's multi-digit.

    # TC:- O(N)
    # SC:- O(N)
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        n=len(strs)
        encoded=[]
        for i in range(0,n):
            wordLen = len(strs[i])
            encoded.append(str(wordLen)+"#"+strs[i])
        
        return "".join(encoded)


    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        n=len(s)
        ans=[]
        i=0

        while i<n:
            j=i
            while s[j]!="#":
                j+=1
            
            length = int(s[i:j])
            ans.append(s[j+1: j+1+length])
            i = j+1+length
        
        return ans



s1 = Solution()
strs=["Hello", "Me"]
s = s1.encode(strs)
print(s1.decode(s))
    

