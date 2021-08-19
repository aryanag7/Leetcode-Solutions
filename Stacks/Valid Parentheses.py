class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False 
        stack=[]
        dict={"(":")","{":"}","[":"]"}
        ans=True
        for i in s:
            if i in dict:
                stack.append(i) 
            else:
                if len(stack)>0 and dict[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
                    
        return len(stack)==0
          
        
       
