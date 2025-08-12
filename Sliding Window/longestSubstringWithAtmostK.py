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
    # TC:- O(N*N)
    # SC:- O(K+1)
    def lengthOfLongestSubstringKDistinct(self, s, k):
        ans=0
        n=len(s)

        for i in range(0,n):
            seen= set()
            for j in range(i,n):
                seen.add(s[j])
                if len(seen)>k:
                    break

                ans= max(ans,j-i+1)
        
        return ans
    


    # TC:- O(N + N)
    #  SC:- O(K+1)
    def lengthOfLongestSubstringKDistinct(self, s, k):
        ans=0
        n=len(s)

        l=0
        r=0
        d=defaultdict(int)

        while r<n:
            d[s[r]]+=1

            while len(d)>k:
                d[s[l]]-=1
                if d[s[l]]==0:
                    d.pop(s[l])
                l+=1


            ans = max(ans, r-l+1)
            r+=1
        
        return ans


    #can also optimize the while loop to if to not let the window size reduce beyond our ans length. As we are trying to make the ans length to be increased by 1


    
s1 = Solution()
s = "eceba"
k = 2
print(s1.lengthOfLongestSubstringKDistinct(s,k))

    


