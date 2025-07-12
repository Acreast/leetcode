# Last updated: 7/12/2025, 11:43:00 PM
class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if x % 2 else 2 for x in Counter(s).values())