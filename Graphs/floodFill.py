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
    def DFS_traversal(self,image,ans,sr,sc,color,n,m,visited,baseColor):
        visited[sr][sc]=1
        ans[sr][sc] = color

        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        for d in directions:
            i = sr + d[0]
            j = sc + d[1]

            if i>=0 and i<n and j>=0 and j<m and image[i][j]==baseColor and visited[i][j]==0:
                self.DFS_traversal(image,ans,i,j,color,n,m,visited,baseColor)


    # TC:- O(N * M *4)
    # SC:- O(N*M) ans and O(N * M) for visited
    def floodFill(self, image, sr, sc, color):
        n=len(image)
        m=len(image[0])

        visited = [[0 for _ in range(m)] for _ in range(n)]

        ans = [row[:] for row in image]

        if image[sr][sc] == color:
            return image
        
        baseColor = image[sr][sc]
        

        self.DFS_traversal(image,ans,sr,sc,color,n,m,visited,baseColor)

        return ans





    
s1 = Solution()
image =[[1,1,1],[3,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(s1.floodFill(image,sr,sc,color))

    


