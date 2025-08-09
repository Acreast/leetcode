# Last updated: 8/9/2025, 6:34:46 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True
        if n % 2 != 0:
            return False
        
        cur = 2
        while cur < n:
            cur *= 2
            if cur == n:
                return True

        return False