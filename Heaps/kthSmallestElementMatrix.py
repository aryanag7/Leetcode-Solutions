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
  # TC :- o(N*N) + O(N*N log N*N)
  # SC:- O(N*N)
  def kthSmallest(self, matrix, k):
    arr = []
    for row in matrix:
      for ele in row:
        arr.append(ele)
    
    arr.sort()

    return arr[k-1]
  
  #could have also pushed all nodes in pq, n*n log n*n and then popped k times k * log (n*n)
  

  # TC :- o(N*N log K) - heap size is K
  # SC:- O(K)
  def kthSmallest(self, matrix, k):
    maxHeap = []

    for row in matrix:
      for ele in row:
          heapq.heappush(maxHeap,-ele)

          if len(maxHeap) > k:
            heapq.heappop(maxHeap)
    
    return -maxHeap[0]
  




  # K - WAY MERGE SIMILAR TO MERGE K SORTED LISTS
  # TC:- O(N * logN) + O(K * log(N))
  # SC:- O(N) - N is number of rows
  def kthSmallest(self, matrix, k):
    n= len(matrix)
    m= len(matrix[0])

    minHeap = []


    #put each of min from all the sorted lists to keep size O(N) - no of rows
    for i in range(0,n):
      heapq.heappush(minHeap, (matrix[i][0],i,0))
    
    i=0
    #pop k times - 1st smallest, 2nd, 3rd .... kth smallest
    for i in range(0,k):
      cell, row, col = heapq.heappop(minHeap)
      i+=1
      
      if col + 1 < m:
        heapq.heappush(minHeap, (matrix[row][col+1],row,col+1))
    
    return cell

  
  


s1= Solution()
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(s1.kthSmallest(matrix,k))



