# Last updated: 4/21/2025, 10:56:18 PM
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        max_sum = 0
        min_sum = 0
        total = 0
        for d in differences:
            total += d
            max_sum = max(max_sum, total)
            min_sum = min(min_sum, total)

        return max(0, (upper - lower) - (max_sum - min_sum) + 1)