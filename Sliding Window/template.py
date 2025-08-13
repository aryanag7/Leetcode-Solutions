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


# Pattern 1:- Constant window find Something

# Q-> Calculate the max subarray sum in a window of size k

# TC:- O(N * K) - Brute Force
def maxSubarraySum(arr,k):
    n=len(arr)
    ans=0

    for i in range(0,n-k+1):
        s=0
        for j in range(i,i+k):
            s+=arr[j]

        ans=max(ans,s)
    
    return ans




# TC:- O(N )
def slidingWindowTemplate(arr, k):
    n = len(arr)
    if k > n or k == 0:
        return None  # or some appropriate value/error
    

    # Compute sum of first window of size k
    s = 0
    for i in range(k):
        s += arr[i]



    ans = s
    l = 0
    r = k

    # Slide the window from index k to end - l represents value to be removed and r needs to be added so your window is basically l to r-1
    while r < n:
        s -= arr[l]    # remove leftmost element
        l += 1
        s += arr[r]    # add next element to the window
        r += 1
        ans = max(ans, s)

    return ans



arr = [-3, 2, 4, 2, 1 ,7]
print(slidingWindowTemplate(arr,3))








# Pattern 2:- Condition given, find window size

# Q-> Longest Subarray/Substring <Condition> (sum<=k)

# TC:- O(N * N) - Brute Force
def longestSubarray(arr,k):
    n=len(arr)
    ans=0
    for i in range(0,n):
        s=0
        for j in range(i,n):
            s+=arr[j]
            if s<=k:
                ans= max(ans,j-i+1)

            #optimization
            else:
                break
    return ans
        


# shrinking removes bad elements so the window becomes valid again, allowing us to continue growing it later.
# TC:- O(N to move r) + O(N might take 2 out, then 1 more overall N)
def SlidingWindowTemplate2(arr,k):
    l=0
    r=0 #start with window size 1
    ans=0

    s=0
    n=len(arr)
    while r<n: #at the point of loop entering window is from l to r-1
        s+=arr[r]

        while s>k:
            s-= arr[l]
            l+=1

        ans=max(ans,r-l+1)
        r+=1
    
    return ans

# can replace while with if to remove one element from the left so and not beyond that otherwise have to build up again







arr = [2,5,1,7,10]
print(SlidingWindowTemplate2(arr,14))






# Pattern 2:-No of subarrays <Given condition> (sum=k)
# no of subarrays with sum<=k - no of subarrays with sum<= (k-1) 


#Pattern 4:- minimum/shortest window <Condition>
# find a valid window and keep shrinking and calculate if the shrinked window is a valid one