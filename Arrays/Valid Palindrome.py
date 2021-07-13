class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        s=s.lower()
        i=0
        j=len(s)-1
        palindrome=True
        while i<=j:
            if not s[i].isalnum():
                i=i+1
            elif not s[j].isalnum():
                j=j-1
            elif s[i]==s[j]:
                palindrome=True
                i=i+1
                j=j-1
            
            elif s[i]!=s[j]:
                palindrome=False
                break
        return palindrome

        
