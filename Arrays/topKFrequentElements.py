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
    # TC:- O(N log N)
    #SC :- O(N)
    def topKFrequent(self, nums,k):
        frequencyMap = defaultdict(int)

        for num in nums:
            frequencyMap[num]+=1
        
        sortedFreqMap = dict(sorted(frequencyMap.items(), key=lambda x:x[1], reverse= True))


        ans=[]
        for i,(key,value) in enumerate(sortedFreqMap.items()):
            ans.append(key)
            if i+1==k:
                break
        

        return ans
    
 


   


s1 = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(s1.topKFrequent(nums,k))

    


