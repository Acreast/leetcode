# Last updated: 8/19/2026, 1:37:08 AM
1class Solution:
2    def largestInteger(self, nums: List[int], k: int) -> int:
3        freq = [0] * 51
4        for num in nums:
5            freq[num] += 1
6        
7        res, n = - 1, len(nums)
8        for i, c in enumerate(nums):
9            if k == n or (freq[c]==1 and (k==1 or not i or i+1==n)):
10                res = max(res,c)
11        
12        return res