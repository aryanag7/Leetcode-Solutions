# Solution 1
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        for i in range(1,n+1):
            if i in target:
                ans.append("Push")
            else:
                ans.append("Push")
                ans.append("Pop")
            if i == target[-1]:
                break
        return ans
     
# Solution 2
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        input=1
        ans=[]
        for i in target:
            while input<i:
                ans.append("Push")
                ans.append("Pop")
                input+=1
                
                
            
            ans.append("Push")
            input+=1
        return ans

