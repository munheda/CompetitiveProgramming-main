# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.addition=0
        
        def dfs(child,parent,grand_parent):
            if not child:
                return 0
            
            if child:
                if grand_parent and grand_parent.val %2==0:
                    
                    self.addition += child.val
                    
                dfs(child.left,child,parent)
                dfs(child.right,child,parent)
                    
                return self.addition
        return dfs(root, None,None)
        