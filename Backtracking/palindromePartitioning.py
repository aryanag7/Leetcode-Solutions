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
    # state change will be to i+1 as ind till i is what we are adding into the answer
    # TC:O(2^N-1) n-1 paritions and decision at every parition to cut to make a substring  or not cut
    # SC:- Total possible partitioning paths = 2^(N-1) ≈ O(2^N)
    # Each of those 2^N valid answers might contain up to N substrings, e.g., ["a","a","a","a","a"]. 
    # O(2^N × N)

    
    def isPalindrome(self,s):
        return s == s[::-1]



    def partitionHelper(self,s,ind,ds,ans):
        if ind==len(s):
            ans.append(ds)
            return
        


        for i in range(ind,len(s)):
            t=s[ind:i+1]
            if self.isPalindrome(t):
                self.partitionHelper(s,i+1,ds+[t],ans)



    def partition(self, s):
        ind=0
        ans=[]
        self.partitionHelper(s,ind,[],ans)
        return ans



s1 = Solution()
s = "aab"
print(s1.partition(s))

    


