# Last updated: 9/13/2025, 12:06:34 AM
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in "aeiou" for c in s)
