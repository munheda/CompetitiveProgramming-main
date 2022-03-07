testcase = int(input())

nums=[]
for i in range(testcase):
    x=int(input())
    nums.append(x)
    



for i in nums:
    
    st1,st2= 31, 32

    if i<=31:
        print("31")
    elif i==32:
        print("32")
    else:
    
        
        while st1<i:
            st1 += 4
            st2 += 4
            if st1>=i:
                print("31")
                break
            if st2==i:
                print("32")
                break
        
        

        
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

