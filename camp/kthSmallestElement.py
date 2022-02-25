import itertools
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        myheap=[]
          
        for i in matrix:
            myheap.extend(i)

        heapq.heapify(myheap)
        
        while len(myheap)>=k and k>1:
            heapq.heappop(myheap)
            k-=1     
        return heapq.heappop(myheap)