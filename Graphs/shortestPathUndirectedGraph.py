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
    def shortestPath(self, adj, src):
        V = len(adj)
        dist = [float('inf')]*V
        queue = [(src,0)]
        dist[src]=0

        while len(queue)>0:
            node , curr_dist = queue.pop(0)

            for ch in adj[node]:
                new_dist = curr_dist+1

                if new_dist< dist[ch]:
                    dist[ch]=new_dist
                    queue.append((ch, new_dist))
            
        for i in range(0,V):
            if dist[i]==float('inf'):
                dist[i]=-1
        
        return dist







s1 = Solution() 
adj = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]]
src=0
print(s1.shortestPath(adj, src))

    


