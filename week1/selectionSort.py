class Solution: 
    def select(self, arr, i):
        minIndex=i
        for j in range (i, len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex=j
        return minIndex
            
            
        
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
           k=self.select(arr, i)
           
           temp=arr[i]
           arr[i]=arr[k]
           arr[k]=temp