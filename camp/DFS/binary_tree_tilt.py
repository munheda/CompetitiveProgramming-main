# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt = 0
        def dfs(node, tilt):
            if not node:
                return (0,0)
            
            left = dfs(node.left,tilt)
            right = dfs(node.right,tilt)
            pre_sum = left[1] + right[1] + node.val
            tilt = abs(left[1] - right[1]) + left[0] + right[0]
            
            return (tilt, pre_sum)
        return dfs(root, tilt)[0]
            
            
                
            
            
        
            
            
                    
                    