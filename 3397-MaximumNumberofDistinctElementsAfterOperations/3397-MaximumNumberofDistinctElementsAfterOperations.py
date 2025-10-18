# Last updated: 10/18/2025, 12:27:14 PM
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        prev = -10 ** 9 
        res = 0
        nums.sort()
        for num in nums:
            if max(num - k, prev + 1) <= num + k:
                prev = max(num - k, prev + 1)
                res += 1
        return res