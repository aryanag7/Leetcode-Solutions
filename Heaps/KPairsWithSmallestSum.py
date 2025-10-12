import bisect
import sys
import os
import math
from collections import defaultdict
from collections import Counter
from typing import Deque
from collections import deque
from itertools import accumulate, count
import heapq

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Redirect stdin and stdout
sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')



class Solution:
    # TC: - O(N*M) + O(N*M log(N*M))
    # SC:- O(N*M)
    def kSmallestPairs(self, nums1, nums2, k):
        n = len(nums1)
        m= len(nums2)

        pairs = []
        for i in range(0,n):
            for j in range(0,m):
                s=nums1[i] + nums2[j]
                pairs.append((s,(nums1[i],nums2[j])))

        sorted_pairs = sorted(pairs, key= lambda x:x[0])
        ans=[]
        
        for i in range(0,k):
            num1, num2 = sorted_pairs[i][1] 

            ans.append([num1,num2])
        
        return ans

    #if we store all the pairs in heap log(N*M) it would still be the same TC N*M log(N*M) 


    # TC:- better than above but still O(N*M log(K)) - N*M will exceed no of operations in 1 sec 10**7
    # SC:- O(K)
    def kSmallestPairs(self, nums1, nums2, k):
        n = len(nums1)
        m= len(nums2)

        maxHeap = []
        for i in range(0,n):
            for j in range(0,m):
                s=nums1[i] + nums2[j]
                heapq.heappush(maxHeap,(-s,(nums1[i],nums2[j])))

                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
        
        return [[i,j] for s,(i,j) in maxHeap]
    



    # TC:- O(K log(min(len(nums1),k)))
    # SC:- O( min(len(nums1),k))
    def kSmallestPairs(self, nums1, nums2, k):
        n = len(nums1)
        m= len(nums2)

        minHeap = []

        for i in range(min(len(nums1),k)):
            s=nums1[i] + nums2[0]
            heapq.heappush(minHeap,(s, (i,0)))
        
        
        ans= []
        
        for i in range(0,k):
            s,(i,j) = heapq.heappop(minHeap)
            ans.append([nums1[i],nums2[j]])

            if j+1 < m:
                s=nums1[i] + nums2[j+1]
                heapq.heappush(minHeap,(s, (i,j+1)))
        

        return ans

        
s1= Solution()
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(s1.kSmallestPairs(nums1, nums2, k))



