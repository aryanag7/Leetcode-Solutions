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


class DisjointSet:
    def __init__(self,n):
        self.n = n
        self.rank = [0]*(n+1)

        self.parent = [0]*(n+1)
        for i in range(1,n+1):
            self.parent[i]=i
        
        self.size = [1]*(n+1)
        
    
    def findUltimateParent(self,node):
        if node == self.parent[node]:
            return node
        
        val = self.findUltimateParent(self.parent[node])

        self.parent[node] = val

        return val


    def UnionByRank(self,u,v):
        ulti_par_u = self.findUltimateParent(u)
        ulti_par_v = self.findUltimateParent(v)

        if ulti_par_u == ulti_par_v:
            return 

        if self.rank[ulti_par_u]  < self.rank[ulti_par_v]:
            self.parent[ulti_par_u] = ulti_par_v
        
        elif self.rank[ulti_par_v] < self.rank[ulti_par_u]:
            self.parent[ulti_par_v] = ulti_par_u
        
        else:
            self.parent[ulti_par_v] = ulti_par_u
            self.rank[ulti_par_u]+=1

    def UnionBySize(self,u,v):
        ulti_par_u = self.findUltimateParent(u)
        ulti_par_v = self.findUltimateParent(v)

        if self.size[ulti_par_u] < self.size[ulti_par_v]:
            self.parent[ulti_par_u]= ulti_par_v
            self.size[ulti_par_v]+= self.size[ulti_par_u]
        
        else:
            self.parent[ulti_par_v] = ulti_par_u
            self.size[ulti_par_u]+= self.size[ulti_par_v]
        
        

        


class Solution:
    # TC:- O(N * N * 4 alpha)
    # SC:- O(N) - all accounts + o(N) MERGED AND O(ANS)
    def accountsMerge(self, accounts):
        account_map ={}
        n=len(accounts)

        dsu = DisjointSet(n)

        for i in range(0,n):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in account_map:
                    account_map[accounts[i][j]]= i
                else:
                    dsu.UnionBySize(i, account_map[accounts[i][j]])
        
        merged = [[] for _ in range(n)]

        for key in account_map:
            mail = key
            node = account_map[key]

            p = dsu.findUltimateParent(node)

            merged[p].append(mail)
        

        ans= []

        for i in range(0,n):
            if len(merged[i])>0:
                name = accounts[i][0]
                temp = []
                temp.append(name)

                for m in sorted(merged[i]):
                    temp.append(m)

                ans.append(temp)

        
        return ans



        


          



          



    
s1 = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(s1.accountsMerge(accounts))

    


