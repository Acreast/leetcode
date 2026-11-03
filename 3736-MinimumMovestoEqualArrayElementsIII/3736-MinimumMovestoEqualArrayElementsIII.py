# Last updated: 11/3/2026, 11:07:37 PM
1class Solution:
2    def minMoves(self, nums: List[int]) -> int:
3        max_val = max(nums)
4        res = 0
5        for n in nums:
6            res += max_val - n
7        
8        return res