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
    #also can use an index array of size 128 ( 0-127 ) to map small,capita alphabets, digits, symbols, spaces or can have as 256 size for a borader range of input

    # TC: - O(N^2)
    # SC:- O(N)
    # def lengthOfLongestSubstring(self, s):
    #     ans=0
    #     n=len(s)
    #     for i in range(0,n):
    #         seen = set()
    #         for j in range(i,n):
    #             if s[j] in seen:
    #                 break
    #             seen.add(s[j])
    #             ans = max(ans, j-i+1)
        

    #     return ans
    


    # TC:- O(N)
    # SC:- O(N)
    def lengthOfLongestSubstring(self, s):
        l=0
        r=0
        d = defaultdict(int)
        ans=0
        n=len(s)

        while r<n:
            d[s[r]]+=1


            #shrink until window is invalid
            while r-l+1 > len(d):
                d[s[l]]-=1
                if d[s[l]]==0:
                    d.pop(s[l])
                l+=1

            ans=max(ans, r-l+1)
            r+=1


        return ans

    #can also use d to store char and its index and move l to repeating char's index+1






            
 



    


s1 = Solution()
s = "abcabcbb"
print(s1.lengthOfLongestSubstring(s))

    


