class Solution:
    
    def removePalindromeSub(self, s: str) -> int:
        
        
        if s=="":
            return 0
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return 2
            left=left+1
            right=right-1
        return 1
    
