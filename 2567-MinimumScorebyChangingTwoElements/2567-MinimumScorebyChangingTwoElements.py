# Last updated: 11/20/2026, 1:42:49 AM
1class Solution:
2    def minimizeSum(self, nums: List[int]) -> int:
3        small = nsmallest(3, nums)
4        large = nlargest(3, nums)
5        return min(large[0] - small[2], large[1] - small[1], large[2] - small[0])