# Last updated: 8/1/2026, 1:01:24 AM
1class Solution:
2    def minimumPushes(self, word: str) -> int:
3        return sum(f*(i//8+1) for i, f in enumerate(sorted(Counter(word).values(), reverse=True)))