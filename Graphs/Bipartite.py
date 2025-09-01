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
        
    # BFS
    # TC:- O(V+2E) + O (V) for the loop outer
    # SC:- O(V) for colored and O(V) for queue
    # def checkBipartiteBFS(self, graph, src, colored):    
    #     V = len(graph)

    #     colored[src]=0

    #     queue = [src]

    #     while len(queue)>0:
    #         node = queue.pop(0)

    #         for ch in graph[node]:
    #             if not colored[ch]:
    #                 c = not(colored[node])
    #                 colored[ch] = c
    #                 queue.append(ch)
    #             else:
    #                 if colored[node] == colored[ch]:
    #                     return False
        
    #     return True
    


    # DFS
    # TC:- O(V+2E) + O (V) for the loop outer
    # SC:- O(V) for colored and O(V) for stack space
    def checkBipartiteDFS(self, graph, src, col, colored):    
        colored[src]=col

        for ch in graph[src]:
            if not colored[ch]:
                if not self.checkBipartiteDFS(graph, ch, not(colored[src]), colored):
                    return False
            else:
                if colored[src] == colored[ch]:
                    return False
        
        return True


    def isBipartite(self, graph):
        V = len(graph)

        colored = [False]*V

        for i in range(0,V):
            if not colored[i]:
                if not self.checkBipartiteDFS(graph, i,0, colored):
                    return False
        
        return True
                    



    
s1 = Solution() 
graph = [[1,3],[0,2],[1,3],[0,2]]
print(s1.isBipartite(graph))

    


