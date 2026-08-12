# Last updated: 8/13/2026, 1:29:37 AM
1class Solution:
2    def maxSubarrayLength(self, nums, k):
3        m = {}
4
5        i = 0
6        res = 0
7
8        for j in range(len(nums)):
9            m[nums[j]] = m.get(nums[j], 0) + 1
10
11            while m[nums[j]] > k:
12                m[nums[i]] -= 1
13                i += 1
14
15            res = max(res, j - i + 1)
16
17        return res