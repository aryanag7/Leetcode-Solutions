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
    # TC:- O(K+K)
    # SC:- O(1)
    def maxScore(self, cardPoints, k):
        left_sum = 0
        right_sum =0

        for i in range(k):
            left_sum+= cardPoints[i]
        
        ans=left_sum + right_sum
        l= k-1
        r= len(cardPoints)-1

        while l>=0:
            left_sum -= cardPoints[l]
            l-=1

            right_sum += cardPoints[r]
            r-=1

            ans= max(ans, left_sum+right_sum)
        
        return ans


            
 



    


s1 = Solution()
cardPoints = [9,7,7,9,7,7,9]
k = 7
print(s1.maxScore(cardPoints,k))

    


