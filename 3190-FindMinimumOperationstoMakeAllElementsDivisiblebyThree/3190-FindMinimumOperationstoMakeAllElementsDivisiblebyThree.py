# Last updated: 11/22/2025, 4:25:21 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += 1 if num % 3 == 1 or num % 3 == 2 else 0
        return res