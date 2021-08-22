class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if len(stack)>0 and i.upper()==stack[-1].upper():
                if stack[-1]!=i:
                    stack.pop()
                else:
                    stack.append(i)
          
            else:
                stack.append(i)
        return "".join(stack)
   
