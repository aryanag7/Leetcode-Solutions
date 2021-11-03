
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        self.traversal(root,ans)
        return ans
        
        
        
    def traversal(self,root,ans):
        if root==None:
            return ans
        ans.append(root.val)
        for child in root.children:
            self.traversal(child,ans)
        
                
        
