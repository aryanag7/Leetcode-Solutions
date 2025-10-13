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



#Assuming MAX-HEAP
#Height of CBT is logN as to accomodate N nodes we will have logN levels; N = 15 , log15 = 3 ; 0->1->2->; 3 jumps

#min nodes for h height h=3 : 2^h
#max nodes for h height h=3 : 2^(h+1) - 1 



class PriorityQueue():
    def __init__(self):
        self.pq=[]

    def getSize(self):
        return len(self.pq)
    
    def isEmpty(self):
        return self.getSize()==0
    
    def swap(self, childIndex, parentIndex):
        self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]

    #heapify is the operation to build a heap (min-heap or max-heap) from an iterable; assume you have a list of numbers which is a CBT, you need to traverse the non leaf nodes from the back and perform down_heapify on each of them. 
    #- why not leaf nodes also? they are single nodes they would be a heap in itself, no need to check them
    #- leaf nodes in CBT ; n//2 to n-1
    #- non leaf nodes in CBt :- 0 to n//2-1

    def build_heap(self,arr):
        n = len(arr)
        
        #non leaf nodes
        for index in range((n//2)-1, -1,-1):
            self.heapify(index,arr,n)

        return arr


    def heapify(self,parentIndex,heap,n):
        while True:
        
            leftIndex=  (2*parentIndex)+1
            rightIndex= (2*parentIndex)+2

            if leftIndex>=n:
                break

            idxToSwap = leftIndex

            if rightIndex < n and heap[rightIndex] > heap[leftIndex]:
                idxToSwap = rightIndex

            
            if heap[idxToSwap] <= heap[parentIndex]:
                break

            heap[parentIndex],heap[idxToSwap]= heap[idxToSwap],heap[parentIndex]

            parentIndex=idxToSwap

    
    # TC:-  #O(N * logN)
    # sc:- O(1) - in place
    def heapSort(self,arr):
        #build max heap out of unsorted array
        #O(N)
        n=len(arr)
        for i in range((n//2)-1,-1,-1):
            self.heapify(i,arr,n)
        
        #O(N * logN)
        for i in range(n-1,0,-1):
            print(arr)
            arr[0], arr[i] =  arr[i], arr[0]
            self.heapify(0,arr,i)

        return arr


        
    
    def up_heapify(self):
        childIndex=len(self.pq)-1

        while childIndex>0:
            parentIndex= (childIndex-1)//2

            if self.pq[childIndex] > self.pq[parentIndex]:
                self.swap(childIndex, parentIndex)
                childIndex = parentIndex

            else:
                break


    # TC:- O(logN) - just append at the last and heapify upwards, propogate to the top which is height of the CBT (logN)
    def insert(self,value):
        self.pq.append(value)
        self.up_heapify()



    def down_heapify(self,parentIndex):
        n=self.getSize()
        while True:
        
            leftIndex=  (2*parentIndex)+1
            rightIndex= (2*parentIndex)+2

            if leftIndex>=n:
                break

            idxToSwap = leftIndex

            if rightIndex < n and self.pq[rightIndex] > self.pq[leftIndex]:
                idxToSwap = rightIndex

            
            if self.pq[idxToSwap] <= self.pq[parentIndex]:
                break

            self.pq[parentIndex],self.pq[idxToSwap]= self.pq[idxToSwap],self.pq[parentIndex]

            parentIndex=idxToSwap

         

    # TC:- O(logN) 
    def removeMin(self):
        ans=self.pq[0]
        self.pq[0],self.pq[-1]=self.pq[-1],self.pq[0]
        self.pq.pop()
        self.down_heapify(0)

        return ans


    # TC:- O(1) 
    def getMin(self):
        if self.isEmpty():
            return None
        
        return self.pq[0].value
    
    def print_heap(self):
        for i in self.pq:
            print(i,end=" ")
        print()

    

    
pq= PriorityQueue()
pq.insert(50)
pq.insert(55)
pq.insert(53)
pq.insert(52)
pq.insert(54)
pq.print_heap()

print(pq.removeMin())
pq.print_heap()


# print(pq.build_heap([54,53,55,52,50]))



#heap sort
# arr = [12, 6, 10, 5, 1, 9]
arr = [5,2,6]
print(pq.heapSort(arr))