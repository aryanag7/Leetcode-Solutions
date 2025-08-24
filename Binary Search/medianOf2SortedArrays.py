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
    # TC:- O(N1 + N2)
    # SC:- O(N1 + N2)
    # def findMedianSortedArrays(self, nums1, nums2):
    #     n=len(nums1)
    #     m=len(nums2)
    #     temp = [0]*(n+m)

    #     i,j,k = 0,0,0

    #     while i<n and j<m:
    #         if nums1[i]<=nums2[j]:
    #             temp[k]=nums1[i]
    #             i+=1
            
    #         else:
    #             temp[k]=nums2[j]
    #             j+=1
            
    #         k+=1

    #     while i<n:
    #         temp[k]=nums1[i]
    #         i+=1
    #         k+=1
        
    #     while j<m:
    #         temp[k]= nums2[j]
    #         j+=1
    #         k+=1

    #     print(temp, len(temp))
    #     l=len(temp)

    #     if l%2!=0:
    #         print("inside")
    #         return temp[l//2]

    #     else:
    #         p= temp[l//2]
    #         q = temp[(l//2)-1]

    #         return (p+q)/2


    # TC:- O(N1 + N2)
    # SC:- O(1)
    def findMedianSortedArrays(self, nums1, nums2):
        n=len(nums1)
        m=len(nums2)
        temp =[0,0]

        i,j,k = 0,0,0

        prev_smaller = None
        while i<n and j<m:
            if nums1[i]<=nums2[j]:
                prev_smaller = nums1[i]
                i+=1

            else:
                prev_smaller = nums2[j]
                j+=1

            if k== ((m+n)//2) - 1:
                temp[1] = prev_smaller

            if k== (m+n)//2:
                temp[0] = prev_smaller
        
            
            k+=1

       

        while i<n:
            if k== (m+n)//2:
                temp[0] =nums1[i]
            
            if k== ((m+n)//2) - 1:
                temp[1] =nums1[i]

            i+=1
            k+=1

        
        while j<m:
            if k== (m+n)//2:
                temp[0]= nums2[j]
            
            if k== ((m+n)//2) - 1:
                temp[1] =nums2[j]

            j+=1
            k+=1
        
        if (m+n)%2!=0:
            return temp[0]

        else:
            return (temp[0]+temp[1])/2
    
    

    def answer(self,n,m,l1,l2,r1,r2):
        if (n+m)%2==0:
            return (max(l1,l2)+  min(r1,r2))/2
        else:
            return max(l1,l2)




    # TC:- O(LOG(N1 SMALLER ONE)
    # SC:- O(1)
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1 , nums2 = nums2, nums1
        
        n=len(nums1) #smamler one always
        m=len(nums2)

        low = 0
        high = n

        total_elements = (n+m+1)//2

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
                return self.answer(n,m,l1,l2,r1,r2)
            
            if l1 > r2:
                high = mid1 -1
            
            elif l2 > r1:
                low = mid1+1
            
    
s1 = Solution()
nums1=[1,3]
nums2= [2]
print(s1.findMedianSortedArrays(nums1,nums2))

    




