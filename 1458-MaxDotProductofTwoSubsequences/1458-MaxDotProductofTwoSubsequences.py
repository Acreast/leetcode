# Last updated: 1/9/2026, 12:06:02 AM
1class Solution:
2    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
3        
4        cache = {}
5
6        def dp(i, j):
7            if i == len(nums1) or j == len(nums2):
8                return float("-inf")
9            
10            if (i,j) in cache:
11                return cache[(i, j)]
12            
13            take = nums1[i] * nums2[j]
14            res = max(
15                take + dp(i + 1, j + 1),
16                take,
17                dp(i + 1, j),
18                dp(i, j + 1)
19            )
20            cache[(i,j)] = res
21            return cache[(i,j)]
22
23
24        return dp(0,0)