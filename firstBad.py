# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
            
        left = 1

        right = n 
        
        bad = -1

        while left <= right:
            
            print(right)

            mid  = (right + left )//2

            if isBadVersion(mid):
                right = mid - 1
                bad = mid

            else:
                left = mid + 1

        return bad

