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
    # TC:- O(N) + O(NlogN)
    # sc:- O(N)
    def kClosest(self, points, k):
        d = []

        for point in points:
            x = point[0]
            y = point[1]

            dist = math.sqrt((x-0)*(x-0) + (y-0)*(y-0))

            d.append(((x,y),dist))
        
        print(d)
        d.sort(key= lambda x:x[1])
 

        ans=[]
        for i in range(0,k):
            ans.append(d[i][0])
        
        return 
    

    # TC:- O(N) + O(NlogK)
    # sc:- O(N) + O(K)
    #can also do in single pass calculation of dist and heap manipulation
    def kClosest(self, points, k):
        d = []

        for point in points:
            x = point[0]
            y = point[1]

            dist = math.sqrt((x-0)*(x-0) + (y-0)*(y-0))

            d.append(((x,y),dist))

        maxHeap = []
        n=len(points)
        for i in range(0,n):
            if len(maxHeap)<k:
                heapq.heappush(maxHeap,(-d[i][1],d[i][0]))
            
            elif d[i][1] < -maxHeap[0][0]:
                heapq.heapreplace(maxHeap,(-d[i][1],d[i][0]))
        
        return [ coordinate  for _, coordinate in maxHeap]
        
    



s1= Solution()
points = [[1,3],[-2,2]]
k = 1
print(s1.kClosest(points,k))



