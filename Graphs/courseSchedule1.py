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
    # TC:- O(V + E)
    # SC:- O(V) + O(V) + O(V)
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        inDegree = [0]*numCourses


        for prereq in prerequisites:
            u=prereq[0]
            v= prereq[1]

            adj[v].append(u)
            inDegree[u]+=1

        queue = []
        for i in range(0,numCourses):
            if inDegree[i]==0:
                queue.append(i)
        

        count=0
        while len(queue)>0:
            node = queue.pop(0)
            count+=1

            for ch in adj[node]:
                inDegree[ch]-=1
                if inDegree[ch]==0:
                    queue.append(ch)
        
        if count == numCourses:
            return True
        return False


        


        


    
s1 = Solution() 
numCourses = 2
prerequisites =[[1,0],[0,1]]
print(s1.canFinish(numCourses,prerequisites))

    


