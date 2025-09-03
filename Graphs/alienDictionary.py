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
    def alienOrder(self, words):
        unique = set("".join(words))
        adj = { c:[] for c in unique}

        n = len(words)
        for i in range(0,n-1):
            word1= words[i]
            word2 = words[i+1]

            if len(word1)>len(word2):
                return ""

            j=0
            k=0

            while j< len(word1) and k<len(word2):
                if word1[j]!=word2[k]:
                    adj[word1[j]].append(word2[k])
                    break
        
                j+=1
                k+=1
        

        
        inDegree = {c:0 for c in unique}
        for node in adj:
            for c in adj[node]:
                inDegree[c]+=1
        
        
        queue=[]
        for c in inDegree:
            if inDegree[c]==0:
                queue.append(c)
        

        ans=""
        while len(queue)>0:
            char = queue.pop()
            ans+= char

            for ch in adj[char]:
                inDegree[ch]-=1
                if inDegree[ch]==0:
                    queue.append(ch)

        print(ans)
        if len(ans) == len(unique):
            return ans

        return ""       

        
        


s1 = Solution() 
words = ["z","x","z"]
print(s1.alienOrder(words))

    


