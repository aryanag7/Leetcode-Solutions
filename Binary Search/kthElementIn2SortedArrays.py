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
    # TC:- O(N1+N2)
    # SC:- O(N1+N2)
    # def kthElement(self, nums1, nums2, k):
    #     n=len(nums1)
    #     m=len(nums2)
    #     temp = [0]*(n+m)

    #     i,j,p = 0,0,0

    #     while i<n and j<m:
    #         if nums1[i]<=nums2[j]:
    #             temp[p]=nums1[i]
    #             i+=1
            
    #         else:
    #             temp[p]=nums2[j]
    #             j+=1
            
    #         p+=1

    #     while i<n:
    #         temp[p]=nums1[i]
    #         i+=1
    #         p+=1
        
    #     while j<m:
    #         temp[p]= nums2[j]
    #         j+=1
    #         p+=1
        
    #     return temp[k-1]
    

    # TC:- O(N1+N2)
    # SC:- O(1) no space
    # def kthElement(self, nums1, nums2, k):
    #     n=len(nums1)
    #     m=len(nums2)

    #     i,j,p = 0,0,0

    #     prev_smaller = None

    #     while i<n and j<m:
    #         if nums1[i]<=nums2[j]:
    #             prev_smaller = nums1[i]
    #             i+=1
            
    #         else:
    #             prev_smaller= nums2[j]
    #             j+=1

    #         if p==k-1:
    #             return prev_smaller
            
    #         p+=1

    #     while i<n:
    #         i+=1
    #         if p==k-1:
    #             return nums1[i]
    #         p+=1
        
    #     while j<m:
    #         j+=1
    #         if p==k-1:
    #             return nums2[j]
    #         p+=1






    # TC:- O(LOG(N1 SMALLER ONE)
    # SC:- O(1)
    def kthElement(self, nums1, nums2,k):
        if len(nums1)>len(nums2):
            nums1 , nums2 = nums2, nums1
        
        n=len(nums1) #smamler one always
        m=len(nums2)

        low = max(0, k-m)
        high = min(n,k)

        total_elements = k

        while low<= high:
            mid1 = low + (high-low)//2
            mid2 = total_elements - mid1

            l1= float('-inf')
            l2= float('-inf')
            r1= float('inf')
            r2= float('inf')

            if mid1<n:
                r1= nums1[mid1]
            if mid2<m:
                r2= nums2[mid2]
            
            if mid1-1>=0:
                l1 = nums1[mid1-1]
            if mid2-1>=0:
                l2 = nums2[mid2-1]
            
            if max(l1,l2)<= min(r1,r2):
                print(mid1)
                return max(l1,l2)
            
            if l1 > r2:
                high = mid1 -1
            
            elif l2 > r1:
                low = mid1+1
        
            
s1 = Solution()
nums1=[2, 3, 6, 7, 9]
nums2= [1, 4, 8, 10]
print(s1.kthElement(nums1,nums2,5))

    




