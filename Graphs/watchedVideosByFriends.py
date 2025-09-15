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
    def watchedVideosByFriends(self, watchedVideos,friends, id, level):
        V = len(watchedVideos)
        adj =friends

        queue = [(0,id)]
        visited = [0]*V
        visited[id] = 1

        watched_freq = defaultdict(int)

        while len(queue)>0:
            curr_level, node = queue.pop(0)

            if curr_level == level:
                for v in watchedVideos[node]:
                    watched_freq[v]+=1
                continue


            for ch in adj[node]:
                if visited[ch]==0:
                    queue.append((curr_level+1,ch))
                    visited[ch]=1
        
        
        ans = [t[0] for t in  sorted(watched_freq.items(), key= lambda x:(x[1],x[0]))]

        return ans
        

        




s1 = Solution() 
watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 1
print(s1.watchedVideosByFriends(watchedVideos,friends, id, level))

    


