class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n=len(citations)
        hin=0
        left=0
        right=n-1

        # mid=(right+left)//2
        
        while left<=right:
            
            mid=left+ (right-left)//2
            
            hin=mid
            
            if citations[mid] <(n-mid):
                left=mid+1
                
            elif citations[mid]>(n-mid):
                right=mid-1
                
            elif citations[mid]==(n-mid):
                return n-mid
  
            
            
        return n-left
       
                
        
        