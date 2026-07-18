# Last updated: 7/19/2026, 1:01:34 AM
1class Solution:
2    def findGCD(self, nums: List[int]) -> int:
3        return gcd(min(nums), max(nums))
4