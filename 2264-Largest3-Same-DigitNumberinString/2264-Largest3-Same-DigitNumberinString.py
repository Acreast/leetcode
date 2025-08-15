# Last updated: 8/15/2025, 11:19:49 PM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n & (n - 1)) == 0 and n % 3 == 1