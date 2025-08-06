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
    # TC :- O(N * KLOGK)
    # SC :- O(N * K)
    def groupAnagrams(self, strs):
        anagramList = defaultdict(list)


        for s in strs:
            sortedS = "".join(sorted(s))
            anagramList[sortedS].append(s)

        ans=[]
        for key in anagramList:
            ans.append(anagramList[key])
        
        return ans
    
    
    
    # TC :- O(N * K)
    # SC :- O(N * K)
    def groupAnagrams(self, strs):
        anagramList = defaultdict(list)


        for s in strs:
            count=[0]*26
            for char in s:
                idx = ord(char) - ord('a')
                count[idx]+=1
            
            key = tuple(count)
            anagramList[key].append(s)
        
        print(anagramList)



        ans=[]
        for key in anagramList:
            ans.append(anagramList[key])
        
        return ans
   


s1 = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s1.groupAnagrams(strs))

    


