# Last updated: 10/19/2026, 9:10:14 PM
1class Solution:
2    def targetIndices(self, nums: list[int], target: int) -> list[int]:
3        nums.sort()
4        res = []
5        for i, n in enumerate(nums):
6            if n == target:
7                res.append(i)
8        
9        return res
10
11