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
    # Adjacency matrix to store graph
    #SC:- O(N^N) - COSTLY!
    def adjMatrix(self,n,m):
        adj = [[ 0 for j in range(n+1)] for i in range(n+1)]

        for i in range(0,m):
            u,v=list(map(int,input().split()))
            adj[u][v]=1
            adj[v][u]=1
        
        return adj
    


    # Adjacency list to store graph
    #SC:- O(2 * E) - as every edge is connected to 2 nodes.
    def adjList(self,n,m):
        adj =[[] for _ in range(n+1)]


        for _ in range(0,m):
            u,v=list(map(int,input().split()))
            adj[u].append(v)
            # if its directed then no need for v --> u
            adj[v].append(u)

        return adj
    
    #Adj lists are better in most of the cases because of the less space complexity as well as the time complexity to traverse;
    # O( N +2E) as we are not iterating 2e edges everytime, for each node we are going through its connected nodes sometimes 1, sometimes 3 totalling 2E edges

    #for weighted graph , store pairs in adj list of (v,wt) and in matrix you can store wt at mat[u][v] = wt so if it's !=0 it means its conneted with weight stored there



    # TC:- O(N+2E)
    # SC:- O(3N) each for queue, ans and visited array
    def bfs(self, adj):
        V = len(adj)
        visited = [0]*V
        ans = []
        queue =[(0,0)]
        visited[0]=1

        #o(n)
        while len(queue)>0:
            node, lvl = queue.pop(0)
            ans.append(node)
            
            #o(2e)
            for ch in adj[node]:
                if visited[ch]==0:
                    queue.append((ch,lvl+1))
                    visited[ch]=1
        
        return ans
    


    # TC:- O(N+2E) - for undirected
    # SC:- O(3N) each for stack space (if skewed), ans and visited array
    def dfs(self, adj):
        V = len(adj)
        visited = [0]*V

        dfs = []

        def Dfs_traversal(src, adj, visited, V):
            dfs.append(src)
            visited[src]=1

            for ch in adj[src]:
                if visited[ch]==0:
                    Dfs_traversal(ch, adj, visited, V)

        Dfs_traversal(0, adj, visited, V)

        return dfs




   


   

    
s1 = Solution()
adj= [[2, 3, 1], [0], [0, 4], [0], [2]]
print(s1.dfs(adj))

    


