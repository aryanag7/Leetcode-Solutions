def solve(nums,index):
    ans=[]
    # j=0
    # for i in nums:
    #     ans.insert(index[j],i)
    #     j=j+1
        
    for i,j in zip(index,nums):
        ans.insert(i,j)
    
    return ans   
     
  

nums=list(map(int,input().split()))
index=list(map(int,input().split()))
print(solve(nums,index))
