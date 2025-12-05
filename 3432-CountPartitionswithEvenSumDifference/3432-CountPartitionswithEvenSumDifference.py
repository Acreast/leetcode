# Last updated: 12/6/2025, 12:20:23 AM
1class Solution:
2    def countPartitions(self, nums: List[int]) -> int:
3        total = sum(nums)
4        if total % 2 != 0:
5            return 0
6        return len(nums) - 1
7                