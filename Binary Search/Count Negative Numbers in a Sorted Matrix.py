# Linear Search O(N)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for row in grid:
            for ele in row:
                if ele<0:
                    count+=1
        return count
        
#Binary Search O(NLOGN)
class Solution:
    def binary_search(self,row):
        i=0
        j=len(row)-1
    
        while i<=j:
            mid=(i+j)//2
            if row[mid]<0:
                j=mid-1
            elif row[mid]>0:
                i=mid+1
                
        return len(row)-i
                
                
        
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for row in grid:
            count+=self.binary_search(row)
        return count
       
        
        
#Using 2 pointers O(M+N)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        i=0
        j=n-1
        count=0
        while i<m and j>=0:
            if grid[i][j]<0:
                count+=(m-i)
                j=j-1
            else:
                i=i+1
        return count
