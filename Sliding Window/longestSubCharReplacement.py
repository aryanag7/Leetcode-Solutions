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
    # TC:- O(N* N)
    # SC:- O(26)
    # def characterReplacement(self, s,k):
    #     ans=0
    #     n=len(s)

    #     # trying to keep the max frequency character and replacing all other in window if operations <=k.
    #     for i in range(0,n):
    #         d = defaultdict(int)
    #         maxFreq = 0
    #         for j in range(i,n):
    #             d[s[j]]+=1

    #             maxFreq = max(maxFreq,d[s[j]])

    #             changes = (j-i+1) - maxFreq
    #             if changes>k:

    #                 break
    #             ans = max(ans, j-i+1)
        
    #     return ans
    

    
    # TC:- O(N + N) * 26
    # SC:- O(26)
    def characterReplacement(self, s,k):
        ans=0
        n=len(s)

        l=0
        r=0
        d= defaultdict(int)
        maxFreq = 0

        while r<n:
            d[s[r]]+=1
            maxFreq = max(maxFreq, d[s[r]])

            while (r-l+1) - maxFreq >k:
                d[s[l]]-=1
                if d[s[l]]==0:
                    d.pop(s[l])
                
                for key in d:
                    maxFreq = max(maxFreq, d[key] )
                l+=1

            ans = max(ans, r-l+1)
            r+=1
        

        return ans
    

    
    # We keep maxFreq as the highest frequency seen so far to avoid costly recalculations when shrinking. Even if it’s outdated, shrinking the window ensures correctness and helps find the longest valid substring efficiently.
    # TC:- O(N)
    # SC:- O(26)
    def characterReplacement(self, s,k):
        ans=0
        n=len(s)

        l=0
        r=0
        d= defaultdict(int)
        maxFreq = 0

        while r<n:
            d[s[r]]+=1
            maxFreq = max(maxFreq, d[s[r]])

            if (r-l+1) - maxFreq >k:
                d[s[l]]-=1
                if d[s[l]]==0:
                    d.pop(s[l])
                
                l+=1

            if (r-l+1) - maxFreq <=k:
                ans = max(ans, r-l+1)
            r+=1
        

        return ans

s1 = Solution()
s = "ABBB"
k = 2
print(s1.characterReplacement(s,k))

    


