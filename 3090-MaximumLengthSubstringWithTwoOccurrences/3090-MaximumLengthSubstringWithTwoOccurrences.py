# Last updated: 8/16/2026, 1:32:25 AM
1class Solution:
2    def longestSubsequence(self, nums: list[int]) -> int:
3        tot = nz = 0
4
5        for n in nums:
6            nz |= n > 0
7            tot ^= n
8
9        return nz * (len(nums) - (not tot))