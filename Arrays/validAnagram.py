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
    # SC:- O(N) + O(N) ~ O(26) if just letters
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s)!=len(t):
    #         return False
    #     sMap= defaultdict(int)
    #     for i in s:
    #         sMap[i]+=1
        
    #     tMap= defaultdict(int)
    #     for i in t:
    #         tMap[i]+=1
        
    #     for key in sMap:
    #         if key not in tMap or sMap[key]!=tMap[key]:
    #             return False
        # return True
    
    def isAnagram(self, s: str, t: str) -> bool:
        # TC:- O(N)
        # SC:- O(N) O(26) if just letters
        sMap= defaultdict(int)

        for i in s:
            sMap[i]+=1

        print(sMap)
        
        for i in t:
            sMap[i]-=1
            if sMap[i]==0:
                sMap.pop(i)
        
        return len(sMap)==0
    
    """
    Unicode is a universal standard that assigns a unique number to every character from every language, allowing consistent text representation across different systems.

    Unicode normalization is the process of converting text to a canonical internal form so that visually identical characters with different underlying code point sequences compare equal. For example, ‘é’ can appear as a single precomposed code point (U+00E9) or as e + combining acute accent (U+0065 + U+0301); without normalization those are different strings. The fix is to normalize both inputs before comparing or counting. In Python I’d 
    
    do:
    import unicodedata
    s = unicodedata.normalize('NFC', s)
    t = unicodedata.normalize('NFC', t)
    This converts both to the composed form (NFC), so canonically equivalent sequences become identical and things like anagram checks or equality work reliably. There are other forms (NFD for decomposed, NFKC/NFKD for compatibility), but NFC is usually a safe default for comparison.”

    NFC:- This is the composed form. Characters with accents are combined into a single character. For example, "é" is one single combined character.

    NFD:- This is the decomposed form. Characters with accents or other marks are split into separate parts.For example, the letter "é" is split into "e" + "´" (a separate accent mark).
    """
        
        
        
   


s1 = Solution()
s = "a"
t = "aa"
print(s1.isAnagram(s,t))

    


