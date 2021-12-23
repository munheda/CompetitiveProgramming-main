class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=[]
        count=0
        
        for i in nums:
            for j in nums:
                if(i>j):
                    count+=1
            
            temp.append(count)
            
            count=0
            
        return temp