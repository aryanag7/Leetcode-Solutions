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



class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        
    #O(1) per call
    def set(self, key, value, timestamp) -> None:
        self.d[key].append((value,timestamp))


    #linear seach each get call is O(N) if N is 10^5 and there are 10^5 get calls so 10^5 x 10^5
    def get(self, key: str, timestamp: int) -> str:
        ans=""

        for pair in self.d[key]:
            val=pair[0]
            t = pair[1]

            if t<=timestamp:
                ans = val
        
        return ans
    

    #IN PYTHON 10^7 OPERATIONS IN 1 SECOND UNLIKE C++ 10^8 OPERATIONS IN 1 SEC.


    #O(log(N)) per call, worst case; 10^5(set calls) + 10^5 * log(10^5) 
    def get(self, key: str, timestamp: int) -> str:
        low=0
        high = len(self.d[key])-1
        ans=""

        while low<= high:
            mid = low+ (high-low)//2
            
            val, t = self.d[key][mid] 

            if t<= timestamp:
                ans = val
                low = mid+1
            else:
                high = mid-1
        
        return ans

        
        




        
            

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo","bar",1)
ans1 = obj.get("foo",1)
ans2 = obj.get("foo",3)
obj.set("foo","bar2",4)
ans3 = obj.get("foo",4)
ans4 = obj.get("foo",5)
print(ans1,ans2,ans3,ans4)

    




