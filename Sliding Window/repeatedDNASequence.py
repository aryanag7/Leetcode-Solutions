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
    # SC:- O(N) 10 length strings + O(N)
    def findRepeatedDnaSequences(self, s: str):
        n = len(s)
        seen = set()
        ans = set()

        for i in range(n-10+1):
            dna = ""
            for j in range(i,i+10):
                dna+= s[j]
            
            if dna in seen:
                ans.add(dna)
            else:
                seen.add(dna)
        
        return [ x for x in ans]
    


    # TC:- O(N)
    # SC:- O(N) worst case all 10 lenth strings unique and no match + O(N) (for ans)
    def findRepeatedDnaSequences(self, s: str):
        n = len(s)
        seen = set()
        ans = set()

        dna = ""
        for r in range(10):
            dna+= s[r]
        
        seen.add(dna)
        l=0
        r=10

        while r<n:
            dna+= s[r]
            dna = dna[1:]

            if dna in seen:
                ans.add(dna)
            else:
                seen.add(dna)
            
            r+=1
            l+=1
        
        return [ x for x in ans]
    







s1 = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(s1.findRepeatedDnaSequences(s))

    


