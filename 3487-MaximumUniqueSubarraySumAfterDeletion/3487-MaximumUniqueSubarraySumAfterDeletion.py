# Last updated: 7/25/2025, 11:05:41 PM
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positive_set = set([num for num in nums if num > 0])
        return max(nums) if len(positive_set) == 0 else sum(positive_set)
