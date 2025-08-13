# Last updated: 8/13/2025, 8:10:24 PM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
    
        cur = 3
        if n == 1:
            return True
        while cur <= n:
            
            if cur == n:
                return True
            cur = cur * 3
        
        return False