class Solution:
    def sortSentence(self, s: str) -> str:
        to_sort={}
        sent=s.split(' ')
        
        for word in sent:
           
            to_sort[int(word[-1])]=word
        val= sorted(to_sort)
        digits="0123456789"
        result=""
        for i in val:
            if to_sort[i][-1] in digits:
                new=to_sort[i].split(to_sort[i][-1])
                result+=new[0]
            result += " "
        res = result.rstrip()
                
        
        return res
            
            
            
            
            
        
        
        
        
        