from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_counter=Counter(nums)
        my_heap=[]
        
        
        for key,val in my_counter.items():
            
            heapq.heappush(my_heap,(-val,key))

        ans=[]
        i=0
        while i <k:
            kthFreq=heapq.heappop(my_heap)
            
            ans.append(kthFreq[1])

            i+=1
            
        return ans