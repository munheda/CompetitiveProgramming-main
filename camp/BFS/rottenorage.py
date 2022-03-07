class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        nofresh = 0
        time = 0
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
                    
                if grid[i][j]==1:
                    nofresh +=1
        while queue and nofresh > 0:
            size = len(queue)
            for i in range(size):
                current= queue.popleft()
                visited.add(current)
                
                for d in directions:
                    nr,nc = current[0] + d[0],current[1] + d[1]
                    if  0<= nr < len(grid) and 0<= nc < len(grid[0]) and grid[nr][nc]==1 and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        grid[nr][nc]= 2
                        nofresh-=1
                        print(nofresh)
            time +=1
        return time if nofresh == 0 else -1
