class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        op= {'(', '{', '['}
        parenthesis= {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in op:
                stack.append(i)
            else:
                if len(stack)==0 or parenthesis[i]!=stack[-1]:
                    return False
                else:
                    stack.pop()
        
        return len(stack)==0