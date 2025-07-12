# Last updated: 7/12/2025, 11:46:08 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        res = 0
        size = 0
        for n in nums:
            if n == target:
                size += 1
            else:
                size = 0
            res = max(res, size)
        return res