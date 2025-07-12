# Last updated: 7/12/2025, 11:42:14 PM
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        for i in range(len(nums) - 1):
            max_diff = max(abs(nums[i] - nums[i + 1]), max_diff)
        return max(abs(nums[-1] - nums[0]), max_diff)
