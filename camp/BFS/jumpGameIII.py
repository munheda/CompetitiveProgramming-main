class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited=set()
        visited.add(start)
        
        
        def dfs(index):
            if arr[index]==0:
                return True
            else:
                if (index + arr[index]) < len(arr) and (index + arr[index]) not in visited:
                    visited.add(index + arr[index])
                    # print(visited)
                    return dfs(index + arr[index])
                if (index - arr[index]) >=0 and (index - arr[index]) not in visited:
                    visited.add(index - arr[index])
                    print(visited)
                    return dfs(index - arr[index])
            return False 
        return dfs(start)
    
                
