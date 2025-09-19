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
    def dfs(self, start, adj, visitedEdges , ds, ans, total):
        ds.append(start)

        
        if len(ds) == total:
            ans.append(ds.copy())
            return True

    

        for i,ch in enumerate(adj[start]):
            if (start,i) not in visitedEdges:
                visitedEdges.add((start,i))
                if self.dfs(ch, adj, visitedEdges , ds, ans, total ):
                    return True

                visitedEdges.remove((start,i))
                
        ds.pop()
        return False


    # TC:- O(E+) O( ELOGE) + worst case O(E!).
    # SC:- O(E) + O(E) + O{E}
    """
    ATL has: [AAA, BBB, CCC]  (loop order is always AAA, then BBB, then CCC)

First visit to ATL (top level):
  pick AAA  -> recurse to AAA ... eventually returns to ATL
Second visit to ATL (remaining {BBB, CCC}, loop order: BBB then CCC):
  try BBB first ...
    if that whole subtree later fails somewhere else, we backtrack to this visit:
  then try CCC ...

Back at top level (backtracked because AAA-first branch didn’t yield a full itinerary):
  pick BBB  -> recurse ... return to ATL
Next visit to ATL (remaining {AAA, CCC}, loop order: AAA then CCC):
  try AAA first, if fail later, then CCC
    
    """
    # def findItinerary(self, tickets):
    #     src = "JFK"
        
    #     adj = defaultdict(list)

    #     for ticket in tickets:
    #         u = ticket[0]
    #         v = ticket[1]
    #         adj[u].append(v)
        
    #     for city in adj:
    #         adj[city].sort()
        
    #     print(adj)
        
    
    #     ans= []

    #     visitedEdges = set()

    #     self.dfs("JFK", adj, visitedEdges , [], ans, len(tickets)+1)

    #     # ans.sort()
    #     return ans[0]










    """
    Eulerian path (trail) = a walk that uses every edge exactly once.
    Use cases: reconstruct itineraries, draw shapes with one stroke, route/postman problems.
    Existence:
    - Undirected: 0(eulerian cycle) or 2 odd-degree vertices (and connected), all others even degree vertices.
    - Directed: start has out - in = 1 (1 extra outgoing edge), end has in - out = 1 (1 extra incoming edge), all others in=out (and weakly connected).
    - only possible if it it's a Single Component Graph

    Hierholzer's Algo(stack) in 2 lines - Directed Graph:
    - start a Dfs anbd check if there are any unvisited neighbours (dfs on that)
    - if not then add into a stack to get the path from end and backtrack to start
    # Path is built in reverse during backtracking → reverse it at the end.
    """


    # TC:- E log E + O(E) (visits each edge once)
    # SC:- O(V+E) + O(E)
    def findItinerary(self, tickets):
        src = "JFK"
        
        adj = defaultdict(list)

        for ticket in tickets:
            u = ticket[0]
            v = ticket[1]
            adj[u].append(v)
        
        for city in adj:
            adj[city].sort(reverse=True) # adj[city].sort()

        

        ans = []

        
        def dfs(node):

            while adj[node]:
                ch = adj[node][-1] #ch = adj[node][0]
                adj[node].pop()   # adj[node].pop(0)
                dfs(ch)
            
            ans.append(node)

        dfs(src)

        return ans[::-1]
    


s1 = Solution() 
tickets =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(s1.findItinerary(tickets))

    


