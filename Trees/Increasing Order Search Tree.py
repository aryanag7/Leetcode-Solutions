class Solution:
    def preorder_trav(self,root,ans):
        if root==None:
            return
        self.preorder_trav(root.left,ans)
        ans.append(root.val)
        self.preorder_trav(root.right,ans)
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans=[]
        self.preorder_trav(root,ans)
        root=TreeNode(ans[0])
        head=root
        for i in range(1,len(ans)):
            root.right=TreeNode(ans[i])
            root=root.right
        return head
        
