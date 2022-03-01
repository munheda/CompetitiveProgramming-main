# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        prevSum=0
        
        def dfs(node,prevSum,targetSum):
            
            
            if node:
                prevSum+=node.val
                
                if node.left==node.right and prevSum==targetSum:
                    return True
                
                return dfs(node.left, prevSum, targetSum) or dfs(node.right, prevSum, targetSum)

            if not node:
                return False

            
        return dfs(root, prevSum,targetSum)
        
        
    