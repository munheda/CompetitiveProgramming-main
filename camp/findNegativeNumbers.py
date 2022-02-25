class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in grid:
            
            left=0
            right=len(i)

            
            while left < right:
                
                mid=(left+right)//2
                
                if i[mid]<0:
                    right=mid        
                else:
                    left=mid+1
                    
            count += len(i)-right
                    
                    
                    
        return count
        
                
            

                
                