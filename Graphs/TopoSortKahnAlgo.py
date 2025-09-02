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
    def topoSort(self, V,E, edges):
        # TC:- O(V + E)
        # SC:- O(V) + O(V)
        # can also use a counter to count nodes instead of storing all topo in a list
        adj = [[] for _ in range(V)]
        for edge in edges:
            u= edge[0]
            v= edge[1]

            adj[u].append(v)

        inDegree = [0]*V
        for node in adj:
            for ch in node:
                inDegree[ch]+=1
        
        queue=[]
        for i in range(0,V):
            if inDegree[i]==0:
                queue.append(i)
        

        ans=[]
        while len(queue)>0:
            node  = queue.pop(0)
            ans.append(node)

            for ch in adj[node]:
                inDegree[ch]-=1
                if inDegree[ch]==0:
                    queue.append(ch)
        
        return ans



        


    
s1 = Solution() 
V = 4
E = 3
edges = [[3, 0], [1, 0], [2, 0]]
print(s1.topoSort(V, E, edges))

    


