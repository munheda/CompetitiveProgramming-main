class Solution:


    def dfs(self, image, current_row, current_col, removedColor, newColor):
        image[current_row][current_col] = newColor
        for d in range(len(self.DIR)-1):
            new_row, new_col = current_row + self.DIR[d], current_col + self.DIR[d+1]
            if not self.in_bound(new_row, new_col) or image[new_row][new_col] != removedColor:
                continue
            self.dfs(image, new_row, new_col, removedColor, newColor)
        
        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.DIR = (1, 0, -1, 0, 1)
        self.in_bound = lambda row, col: 0 <= row < len(image) and 0 <= col < len(image[0])
        removedColor = image[sr][sc]
        if removedColor != newColor:
            self.dfs(image, sr, sc, removedColor, newColor)
        return image
        
 
        
        
