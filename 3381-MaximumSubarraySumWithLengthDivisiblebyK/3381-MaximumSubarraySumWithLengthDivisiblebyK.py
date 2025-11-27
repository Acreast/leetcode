# Last updated: 11/27/2025, 8:54:47 PM
1class Solution:
2    def maxSubarraySum(self, nums: List[int], k: int) -> int:
3        prefix_min = [float("inf")] * k
4        prefix_min[0] = 0
5        res = float("-inf")
6        total = 0
7
8        for i, n in enumerate(nums):
9            total += n
10            length = i + 1
11            prefix_length = length % k
12            res = max(res, total - prefix_min[prefix_length])
13            prefix_min[prefix_length] = min(prefix_min[prefix_length], total)
14
15        return res