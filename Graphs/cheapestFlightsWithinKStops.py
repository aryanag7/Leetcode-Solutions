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
    #here the primary thing in your queue is stops and not price which is stored in sorted order so the price might be jumbled up so you need to return at the very end and not inside the loop unlike other questions where your primary thing in queue is price or distance then we are sure its the minimum from the source
    # TC:- O(V+ E)
    # SC:- O(V) + O
    def minimumEffortPath(self, n, flights, src, dst, k):
        adj= [[] for _ in range(n)]

        for flight in flights:
            u=  flight[0]
            v = flight[1]
            wt = flight[2]

            adj[u].append((v, wt))
        

        price = [float('inf')]*n
        price[src]=0

        queue = [(0, 0,src)]

        while len(queue)>0:
            stops,priceTillNow,  node = queue.pop(0)
            # if node == dst:
            #     return priceTillNow
            
            if stops == k+1:
                continue

            for ch in adj[node]:                
                if priceTillNow + ch[1] < price[ch[0]]:
                    price[ch[0]] = priceTillNow + ch[1]
                    queue.append((stops+1,  priceTillNow+ch[1], ch[0]))
        
        return price[dst] if price[dst]!=float('inf') else -1




        



  

s1 = Solution() 
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(s1.minimumEffortPath(n,flights,src,dst,k))

    


