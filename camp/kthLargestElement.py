import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.myheap=nums
        
        heapq.heapify(self.myheap)
        print(self.myheap)
        
        
        
        while len(self.myheap)>k:
            heapq.heappop(self.myheap)  #removes the smallest elmenent until size of h is <k

    def add(self, val: int) -> int:
        
        if len(self.myheap) > self.k:
            heapq.heappop(self.myheap)
        elif len(self.myheap)<self.k:
            heapq.heappush(self.myheap,val)

        else:
            heapq.heappushpop(self.myheap,val)
            
        return self.myheap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)