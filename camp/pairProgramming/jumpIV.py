from collections import deque
from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        valVis=set()
        vis =set()
        queue=deque()
        indxs=  defaultdict(list)
        
        for i in range(len(arr)):
            indxs[arr[i]].append(i)
        queue.append((0,0))
        
        while queue:
            
            idx, step= queue.popleft()
            vis.add(idx)
            
            val= arr[idx]
            
    
            
            if idx== len(arr)-1:
                return step
            print((idx,step))
            
            if idx + 1 < len(arr) and (idx + 1) not in vis:
                queue.append((idx+1 , step + 1))
                vis.add(idx+1)
            if idx -1 >= 0  and (idx - 1) not in vis:
                queue.append((idx-1, step + 1))
                vis.add(idx-1)

            if val not in valVis:
                for value in indxs[val]:
                    if value not in vis:
                        queue.append((value, step + 1))
                        vis.add(value)  
                        valVis.add(val)
        return -1
            
        
        
        
        
