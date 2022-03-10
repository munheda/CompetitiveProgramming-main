class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        remember = {}
        
        def staircase(index):
            
            if index >= len(cost):
                return 0
            
            if index in remember:
                return remember[index]
            
            oneStep = staircase( index + 1)
            twoSteps = staircase( index + 2) 
            
            remember[index] = min ( oneStep , twoSteps ) + cost[index]
            
            return remember[index]
            
        return min(staircase(0), staircase(1))