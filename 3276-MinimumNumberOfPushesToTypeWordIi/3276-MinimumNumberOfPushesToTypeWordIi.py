# Last updated: 7/12/2025, 11:43:30 PM
class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(f*(i//8+1) for i, f in enumerate(sorted(Counter(word).values(), reverse=True)))