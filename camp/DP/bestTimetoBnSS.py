class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        answer = 0
        
        def profit(index):
            nonlocal answer
            if index == len(prices)-1:
                return prices[index]
            
            maximum = profit(index+1)
            answer = max( answer, maximum -prices[index])
            
            return max(maximum , prices[index])
        profit(0)  
        return answer 