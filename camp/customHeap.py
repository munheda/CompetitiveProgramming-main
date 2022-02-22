#User function Template for python3

class Solution:
    #The Swap Function
    def swap(self,arr,i1,i2):
        arr[i1], arr[i2]= arr[i2],arr[i1]
    
    
    #The LeftChild Function
    def leftChild(self,i):
        return 2*i+1
        
        
    #The RightChild Function
    def rightChild(self,i):
        return 2*i+2
    
    #The Parent Function
    def parent(self,i):
        return (i-1)//2
        
    #The Get Min Function
    def getMin(self,arr):
        return arr[0]
        

        
    #UpHeap function to maintain heap property up the root
    def upheap(self, arr, n, i):
        if arr[i]<arr[self.parent(i)] and i>0:
            self.swap(arr,i,self.parent(i))
            self.upheap(arr, n, self.parent(i))
            
            
            
    #DownHeap function to maintain heap property up the root
    def downheap(self, arr, n, i):
        minPos=i
        left=self.leftChild(i)
        right=self.rightChild(i)
        
        if(left<n and arr[left]<arr[minPos]):
            minPos=left
            
        if(right<n and arr[right]<arr[minPos]):
            minPos=right
        
        if(i!=minPos):
            self.swap(arr,i,minPos)
            self.downheap(arr,n,minPos)
            
            
            
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        #self.upheap(arr,n,i)
        self.downheap(arr,n,i)
        
    
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n-1,-1,-1):
            self.downheap(arr,n,i)
            
            
            
            
    #The insert Function
    def insert(self,arr,n,val):
        arr[n]=val
        self.upheap(arr,n+1,n)
    
    
    
    #The remove Function
    def remove(self,n,i):
        if (i==n-1):
            arr.pop()
        else:
            self.swap(arr,n-1,i)
            arr.pop()
        self.upheap(arr, n-1, i)
    
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        #print(arr)
        for i in range(n-1, -1, -1):
            self.swap(arr,0,i)
            self.downheap(arr,i,0)
        arr.reverse()
        
        
        
        
        


    





#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends