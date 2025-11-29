# Last updated: 11/29/2025, 1:05:41 PM
1class Solution:
2    def minOperations(self, nums: List[int], k: int) -> int:
3        total = sum(nums)
4        remainder = total % k
5
6        return remainder
7
8        