class Solution:
    def generateTheString(self, n: int) -> str:
        string=""
        if n%2==0:
            while n-1>0:
                string+="a"
                n=n-1
            string+="b"
        else:
       
            while n>0:
                string+="a"
                n=n-1
        return string            
    
        
