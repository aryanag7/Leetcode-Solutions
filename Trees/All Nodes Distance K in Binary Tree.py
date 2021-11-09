# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        path=[]
        self.root_to_node_path(root,path,target)
        ans=[]
        for i in range(0,len(path)):
            if i==0:
                block=None
            else:
                block=path[i-1]
            self.print_below_k(path[i],k-i,block,ans)
        return ans
    def root_to_node_path(self,root,path,target):
        if root==None:
            return 
        if root==target:
            path.append(root)
            return path
        left=self.root_to_node_path(root.left,path,target)
        if left!=None:
            left.append(root)
            return left
   
   
    
        right=self.root_to_node_path(root.right,path,target)
        if right!=None:
            right.append(root)
            return right
        return None
    
       
    def print_below_k(self,root,k,block,ans):
        if root==None or root==block:
            return 
        if k==0:
            ans.append(root.val)
            
        self.print_below_k(root.left,k-1,block,ans)
        self.print_below_k(root.right,k-1,block,ans)
   
       
        
        
