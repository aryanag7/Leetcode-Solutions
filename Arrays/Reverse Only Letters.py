class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        low=0
        high=len(s)-1
        while low<high:
            if not s[low].isalpha():
                low=low+1
            elif not s[high].isalpha():
                high=high-1
            else:
                s[low],s[high]=s[high],s[low]
                low=low+1
                high=high-1
        return "".join(s)               
