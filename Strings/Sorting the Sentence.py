class Solution:
    def sortSentence(self, s: str) -> str:
        
        d = {}
        for i in s.split():
            d[int(i[-1])] = i[:-1]
        ans=""
     
        for i in range(1, len(s.split())+1):
            ans += d[i] + " "
        
        return ans[:-1]
