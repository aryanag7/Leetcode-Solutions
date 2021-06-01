# import sys
# sys.stdout = open('New cp/output.txt', 'w')
# sys.stdin = open('New cp/input.txt', 'r')
# # a=int(input()) #This is for interger as input 
# # a,b,c=map(int,input().split()) #This is for 3 interger as input on same line
# # a=list(map(int,input().split())) #list as input
# #a=int(input()) #string as input
# s=input()
# k=int(input())

stack=[]
        
stack.append([s[0],1])
for i in range(1,len(s)):
    if stack==[]:
        stack.append([s[i],1])
           
           
    if len(stack)>0 and s[i]==stack[-1][0]:
        stack[-1][1]=stack[-1][1]+1
                
                
        if stack[-1][1]==k:
            stack.pop()
                        
                
                
    else:
        stack.append([s[i],1])
                
ans=""
for i in range(0,len(stack)):
    char=stack[i][0]
    count=stack[i][1]
    for j in range(0,count):
        ans=ans+char
print(ans)        

         
