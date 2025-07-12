# Last updated: 7/12/2025, 11:42:15 PM
class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        max_even_count = -1
        max_odd_count = -1
        min_even_count = float("inf")
        min_odd_count = float("inf")
        for char in counter:
            char_count = counter[char]
            if char_count % 2 == 0:
                max_even_count = max(max_even_count, char_count)
                min_even_count = min(min_even_count, char_count)
            else:
                max_odd_count = max(max_odd_count, char_count)
                min_odd_count = min(min_odd_count, char_count)
        return max_odd_count - min_even_count