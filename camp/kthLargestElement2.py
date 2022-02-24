import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:        
        myheap=[]      
        for i in nums:
            heapq.heappush(myheap,-i)
        while len(myheap)>=k and k>1:
            heapq.heappop(myheap)
            k-=1     
        return -heapq.heappop(myheap)
            
            
            