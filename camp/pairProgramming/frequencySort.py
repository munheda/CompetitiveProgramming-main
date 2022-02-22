

class Solution:
    def frequencySort(self, s: str) -> str:
        Count= Counter(s)
        
        maxheap=[]
        
        for key,val in Count.items():
            
            heapq.heappush(maxheap,(-val,key))
        print(maxheap)
            
        result=[]
        
        for i in range (len(maxheap)):
            
            pair=heapq.heappop(maxheap)
            
            result.append(pair[1]*(-1*pair[0]))
            print(result)
            
        return "".join(result) 
            
           
            
            