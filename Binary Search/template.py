import bisect
import sys
import os
import math
from collections import defaultdict
from collections import Counter
from typing import Deque
from collections import deque

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Redirect stdin and stdout
sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')


def binary_search(arr,target):
    n=len(arr)

    low=0
    high = n-1

    while low<=high:
        mid = low + (high-low)//2

        if arr[mid] == target:
            return mid
        
        elif target > arr[mid]:
            low = mid+1
        
        else:
            high = mid -1
    
    return -1
    

#Lower Bound:- smallest index such that arr[ind]>=target
def lower_bound(arr,target):
    low=0
    n=len(arr)
    high = n-1
    ans=n

    while low<=high:
        mid = low+ (high-low)//2

        if arr[mid]>=target:
            ans=mid
            high= mid-1
        else:
            #arr[mid]<target
            low = mid+1
    
    return ans

##CAN USE PYTHON BISECT.BISECT_LEFT(ARR,TARGET)



#Upper Bound:- smallest index such that arr[ind]>target
def upper_bound(arr,target):
    low=0
    n=len(arr)
    high = n-1
    ans=n

    while low<=high:
        mid = low+ (high-low)//2

        if arr[mid]>target:
            ans = mid
            high = mid-1
        else:
            #arr[mid]<=target
            low = mid+1

    
    return ans

##CAN USE PYTHON BISECT.BISECT_RIGHT(ARR,TARGET)





arr = [3,3,3,4,6,7,9,12,16,17]
target=3
print(upper_bound(arr,target))