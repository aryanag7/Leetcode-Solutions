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
    # TC:- O(N * N)
    # SC:- OLEN(S) + O(LEN(T))
    # def minWindow(self, s, t):
    #     t_freq = defaultdict(int)
    #     for i in t:
    #         t_freq[i]+=1

    #     # print(len(t_freq))
        
    #     minLen=float('inf')
    #     ans=""
    #     n=len(s)
    #     for i in range(0,n):
    #         s_freq= defaultdict(int)
    #         charsMatched = 0

    #         for j in range(i,n):
    #             s_freq[s[j]]+=1

    #             if s[j] in t_freq and s_freq[s[j]] == t_freq[s[j]]:
    #                 charsMatched+=1
                

    #             if charsMatched == len(t_freq):
    #                 if j-i+1 > minLen:
    #                     break
                    
    #                 minLen = j-i+1
    #                 ans = s[i:j+1]

        
    #     return ans
    
    # TC:- O(N * N)
    # SC:- O(LEN(T)) - OPTIMIZED FROM 2 MAP TO 1 MAP O(256)
    # def minWindow(self, s: str, t: str) -> str:
    #     t_freq = defaultdict(int)
    #     for ch in t:
    #         t_freq[ch] += 1

    #     n = len(s)
    #     m = len(t)
    #     minLen = float('inf')
    #     ans = ""

    #     for i in range(n):
    #         curr_map = dict(t_freq)  #
    #         cnt = 0 

    #         for j in range(i, n):
    #             ch = s[j]

    #             if ch not in curr_map:
    #                 continue

    #             if curr_map[ch] > 0:
    #                 cnt += 1

    #             curr_map[ch] -= 1

    #             if cnt == m:
    #                 if j - i + 1 < minLen:
    #                     minLen = j - i + 1
    #                     ans = s[i:j+1]
    #                 break 

    #     return ans
    

    # TC:- O(N) + (N+ N)
    # SC:- O(256) (chars)
    def minWindow(self, s, t):
        l=0
        r=0
        ans=""
        minLen = float('inf')

        t_freq= defaultdict(int)
        for i in t:
            t_freq[i]+=1
        
        n=len(s)
        m=len(t) #total no of chars in t which we need to match

        matchingChars = 0

        while r<n:
            if s[r] in t_freq and t_freq[s[r]]>0:
                matchingChars+=1


            t_freq[s[r]]-=1
            
            #valid window
            while matchingChars == m:
                if r-l+1 < minLen:
                    minLen = r-l+1
                    ans = s[l:r+1]


                t_freq[s[l]]+=1
                if t_freq[s[l]]>0:
                    matchingChars-=1
                l+=1


            #invalid window
            r+=1
        
        return ans




s1 = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(s1.minWindow(s,t))

    


