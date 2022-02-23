class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        my_counter=Counter(words)
        print(my_counter)
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
        