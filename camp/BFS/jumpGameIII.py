from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visited = set()
        queue = deque() 
        queue.append(start)
        print(visited)

        while queue:
            val = queue.popleft()
            visited.add(val)
            
            if arr[val]==0:
                return True
            
            if (val + arr[val]) < len(arr) and (val + arr[val]) not in visited:
                queue.append(val + arr[val])
                visited.add(val + arr[val])
                
            if (val - arr[val]) >= 0 and (val - arr[val]) not in visited:
                queue.append(val - arr[val])
                visited.add(val - arr[val])
                
        return False
        
        