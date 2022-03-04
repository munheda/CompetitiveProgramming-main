# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue=deque()
        
        queue.append(root)
        ans=[]
        
        while queue:
            
            total=0
            size=len(queue)
            
            for i in range(size):
                
                current = queue.popleft()
                total += current.val
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                    
            ans.append(total/size)
            
        return ans
                
            