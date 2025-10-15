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
    # TC:- O(N logK) - N is tasks size and K is distinct tasks
    # SC:- O(N) + O(N) - 26 letters
    def leastInterval(self, tasks, n):
        freq_map = defaultdict(int)
        for task in tasks:
            freq_map[task]+=1

        maxHeap = []
        for key in freq_map:
            heapq.heappush(maxHeap,(-freq_map[key], key))
        
        time=0
        
        # O(N)
        while len(maxHeap)>0:
            temp = []
            for i in range(0,n+1):
                if maxHeap:
                    freq,char = heapq.heappop(maxHeap)
                    freq = -freq
                    freq-=1
                    temp.append((freq,char))
            
            for f,c in temp:
                if f>0:
                    heapq.heappush(maxHeap, (-f,c))

            if len(maxHeap)==0:
                time+= len(temp)
            else:
                time+= (n+1)
        
        return time





        
       


  


s1= Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
print(s1.leastInterval(tasks,n))



