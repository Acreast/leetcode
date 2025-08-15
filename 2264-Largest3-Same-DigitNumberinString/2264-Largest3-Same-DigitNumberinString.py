# Last updated: 8/15/2025, 11:19:00 PM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        cur = 4
        if n == 1:
            return True
        while cur <= n:
            
            if cur == n:
                return True
            cur = cur * 4
        
        return False