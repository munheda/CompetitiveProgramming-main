import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        myheap=[]
        heapq.heapify(stones)
        
        for i in stones:
            heapq.heappush(myheap,-i)
        
        destroyed=0
        
        while len(myheap)>=2:
            res1=heapq.heappop(myheap)
            res2=heapq.heappop(myheap)
            
            # print(res1)
           
            
            if res1==res2:
                destroyed=res1-res2
            else:
                destroyed= res2-res1
                heapq.heappush(myheap,-destroyed)
                
        return -1*(heapq.heappop(myheap)) if myheap else 0
                
        
            
            
            
            
            
        
        
        