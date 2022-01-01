class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n==0:
            return 1.0
        elif(n==1):
            return x
        elif(n==-1):
            return 1.0/x
        
        if(n%2==0):
            return self.myPow(x*x, n//2)
        else:
            if(n>0):
                
                return self.myPow(x*x, n//2) * x
            else:
                return self.myPow(x*x, -1*(abs(n)//2)) * (1.0/x)

            
            
        
        
    
    
    
    
    