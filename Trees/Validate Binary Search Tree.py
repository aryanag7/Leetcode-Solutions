#Approach1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_trav(self,root,arr):
        if root==None:
            return arr
        self.inorder_trav(root.left,arr)
        arr.append(root.val)
        self.inorder_trav(root.right,arr)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr=[]
        self.inorder_trav(root,arr)
        for i in range(0,len(arr)-1):
            if arr[i]>=arr[i+1]:
                return False
        return True
     
#Approach2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximim(self,root):
        if root==None:
            return float('-inf')
        left=self.maximim(root.left)
        right=self.maximim(root.right)
        return max(root.val,left,right)
    
    

    def minimum(self,root):
        if root==None:
            return float('inf')
        left=self.minimum(root.left)
        right=self.minimum(root.right)
        return min(root.val,left,right)
 

  
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        maxi=self.maximim(root.left)
        mini=self.minimum(root.right)
        if root.val<=maxi or root.val>=mini:
            return False
        left=self.isValidBST(root.left)
        right=self.isValidBST(root.right)
        if left and right:
            return True
        else:
            return False
        
#Approach3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self,root):
        if root==None:
            return float('inf'),float('-inf'),True
        
        left_min,left_max,left_bal=self.help(root.left)
        right_min,right_max,right_bal=self.help(root.right)
        
        mini=min(root.val,left_min,right_min)
        maxi=max(root.val,left_max,right_max)
        treebst=True
        if root.val<=left_max or root.val>=right_min:
            treebst=False
        
        if not(left_bal) or not(right_bal):
            treebst=False
        
        return mini,maxi,treebst
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini,maxi,ans=self.help(root)
        return ans
       
      
        
        
      
