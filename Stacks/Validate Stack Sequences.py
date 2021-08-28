class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        temp=0
        for i in pushed:
            stack.append(i)
        
            while len(stack)>0 and stack[-1]==popped[temp]:
                stack.pop()
                temp=temp+1
       
        return stack==[]
        
 
