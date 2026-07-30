# Last updated: 7/31/2026, 12:43:27 AM
1class Solution:
2    def minimumPushes(self, word: str) -> int:
3        n = len(word)
4        blocks = n // 8
5        return (blocks * (blocks + 1) * 4) + (n % 8) * (blocks + 1)