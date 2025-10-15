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



# TC:- Worst case N * (N log N) - N*N logN
# class MedianFinder:
#     def __init__(self):
#         self.arr = []
#         self.size = 0
        

#     def addNum(self, num: int) -> None:
#         self.arr.append(num)
#         self.size+=1
        

#     def findMedian(self) -> float:
#         self.arr.sort() #nlogn for sorting

#         #even size of list
#         if (self.size%2)==0:
#             n1 = self.arr[self.size//2]
#             n2 = self.arr[(self.size//2)-1]

#             return (n1+n2)/2
        
#         #odd size of list
#         return self.arr[self.size//2]
    



# TC:- Worst case N * N - as we need to shift N elements to right - binary search is logN
class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        index = bisect.bisect_right(self.arr, num)
        self.arr.insert(index,num)

    def findMedian(self) -> float:
        n= len(self.arr)
        #even size of list
        if (n%2)==0:
            n1 = self.arr[n//2]
            n2 = self.arr[(n//2)-1]

            return (n1+n2)/2
        
        #odd size of list
        return self.arr[n//2]




# TC:- O(N * logN) - assuming N calls better than N*N or N*(N logN)
# SC:- O(N) - each heap holds half elements
class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []      



    # logN
    def addNum(self, num: int) -> None:
        #insert
        if len(self.maxHeap)==0 or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)


        #balance
        if len(self.minHeap) == len(self.maxHeap)+1:
            s = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,-s)
        
        elif len(self.maxHeap) == len(self.minHeap)+2:
            s = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,-s)


    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            n1 = -self.maxHeap[0]
            n2 =  self.minHeap[0]

            return (n1+n2)/2
        
        return -self.maxHeap[0]
    
    


obj = MedianFinder()
obj.addNum(1)
obj.addNum(3)
obj.addNum(5)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(4)
print(obj.findMedian())
obj.addNum(6)
print(obj.findMedian())
obj.addNum(8)
obj.addNum(7)

print(obj.findMedian())




