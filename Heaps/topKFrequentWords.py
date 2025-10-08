import bisect
import sys
import os
import math
from collections import defaultdict
from collections import Counter
from typing import Deque
from collections import deque
from itertools import accumulate
import heapq

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Redirect stdin and stdout
sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')



class Solution:
    # TC:- O(N) + O(NlogN)
    # SC:- O(N)
    def topKFrequent(self, words, k):
        d= defaultdict(int)
        for word in words:
            d[word]+=1
        
        sorted_d = sorted(d.items(), key=lambda x:(-x[1],x[0]))

        print(sorted_d)

        # ans= []
        # for i in range(0,k):
        #     tup = sorted_d[i]
        #     ans.append(tup[0])
        
        # return ans

        ans = [key for key,val in sorted(d.items(), key=lambda x:(-x[1],x[0]))[:k]]
    
        return ans
    

    # TC:- O(N) + O(klogN)
    # SC:- O(N) + O(N)
    def topKFrequent(self, words, k):
        d= defaultdict(int)
        for word in words:
            d[word]+=1

        maxHeap = [ (-freq,word) for word,freq in d.items()]
        heapq.heapify(maxHeap)

        ans=[]
        for i in range(0,k):
            ans.append(heapq.heappop(maxHeap)[1])
        
        return ans







"""
What we did is make a single min-heap whose “smallest” item (the root) is the worst candidate:

Primary key: freq ascending (smaller freq is worse)

Tie-break: word descending (lexicographically larger word is worse)

So it acts like:

“min-heap by freq”

and on ties, “max by word”

…but that’s achieved by a custom comparator (or a crafted key), not by using two heaps.
"""
class CompareWrapper:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word

        return self.freq < other.freq

    
class Solution:
    # TC:- O(NlogK)
    # SC:- O(N) + O(K) 
    def topKFrequent(self,words, k):
        d= defaultdict(int)
        for word in words:
            d[word]+=1

        

        # freq stored in the min heap so worst is min (1,3,4) if a new freq is 2, we replace min (2,3,4)
        # word 
        minHeap = []
        for word, freq in d.items():
            it = CompareWrapper(word,freq)

            if len(minHeap) < k:
                heapq.heappush(minHeap,it)
            
            elif  minHeap[0] < it:
                heapq.heapreplace(minHeap,it)

        
        return [ obj.word for obj in sorted(minHeap,key= lambda obj: (-obj.freq,obj.word))]
            


        


s1= Solution()
words =["aaa","aa","a"]
k=2
print(s1.topKFrequent(words,k))



