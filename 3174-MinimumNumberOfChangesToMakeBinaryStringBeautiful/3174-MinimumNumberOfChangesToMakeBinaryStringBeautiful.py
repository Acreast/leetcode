# Last updated: 7/12/2025, 11:43:55 PM
class Solution:
    def minChanges(self, s: str) -> int:
        l = 0
        swaps = 0
        for r in range(len(s)):
            if s[l] != s[r]:
                if r % 2 != 0:
                    swaps += 1
                l = r

        return swaps