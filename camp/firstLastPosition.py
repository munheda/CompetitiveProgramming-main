class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left=0
        right=len(nums)-1
        
        begin=0
        end=len(nums)-1
        
        first=-1
        second=-1
        answer=[]
  
        while left<=right:


            mid= (right+left)//2
            if nums[mid] >target:
                right=mid-1                
            elif nums[mid]<target:
                left=mid+1
            else:
                
                right=mid-1
                first=mid            
        answer.append(first)
                
        while begin<=end:
            mid= (begin+end)//2
            if nums[mid] >target:
                end=mid-1
            elif nums[mid]<target:
                begin=mid+1
            else:

                begin=mid+1
                second=mid
        answer.append(second)           
        return answer
            
         
                
        
        


       