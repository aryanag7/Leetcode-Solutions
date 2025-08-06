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

    # TC:- O(N^2) for first and last element 
    # SC:- O(1)
    # def productExceptSelf(self, nums):
    #     ans=[]

    #     n=len(nums)
    #     for i in range(0,n):
            
    #         prod1=1
    #         for j in range(0,i):
    #             prod1= prod1 * nums[j]

    #         prod2=1
    #         for j in range(i+1,n):
    #             prod2= prod2 * nums[j]
            
    #         ans.append(prod1*prod2)



    #     return ans


    # TC:- O(N) 
    # SC:- O(2N)    
    def productExceptSelf(self, nums):
        ans=[]
        n=len(nums)

        prefixProd = [1]*n
        prefixProd[0]=nums[0]
        suffixProd = [1] * n
        suffixProd[-1] = nums[-1]

        for i in range(1,n):
            prefixProd[i] = prefixProd[i-1] * nums[i]

        for i in range(n-2,-1,-1):
            suffixProd[i] = suffixProd[i+1] * nums[i]

        for i in range(0,n):
            if i==0:
                val = suffixProd[i+1]
            elif i==n-1:
                val = prefixProd[i-1]
            else:
                val = prefixProd[i-1] * suffixProd[i+1]

            ans.append(val)

        return ans
        
    # TC:- O(N) 
    # SC:- O(1) no space other than output ans space  
    def productExceptSelf(self, nums):
        n=len(nums)
        ans=[1]*n
        ans[0]=nums[0]

        for i in range(1,n):
            ans[i]=ans[i-1]*nums[i]
        
        
        suffixProd=1
        for i in range(n-1,-1,-1):
            if i>0:
                ans[i]= ans[i-1]*suffixProd
            else:
                ans[i] = suffixProd


            suffixProd=suffixProd*nums[i]


        return ans

        
    
   


s1 = Solution()
nums =[1,2,3,4]
print(s1.productExceptSelf(nums))

    


