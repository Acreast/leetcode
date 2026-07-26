# Last updated: 7/27/2026, 1:27:53 AM
1class Solution:
2    def maximumProduct(self, nums: List[int]) -> int:
3        nums.sort()
4        return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])