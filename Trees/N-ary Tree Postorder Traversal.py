class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans=[]
        self.traversal(root,ans)
        return ans
        
    def traversal(self,root,ans):
        if root==None:
            return ans
        for child in root.children:
            self.traversal(child,ans)
            
        ans.append(root.val)
            
        
            
