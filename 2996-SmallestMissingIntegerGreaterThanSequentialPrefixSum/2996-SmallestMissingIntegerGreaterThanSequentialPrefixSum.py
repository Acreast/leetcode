# Last updated: 8/12/2026, 12:15:00 AM
1class Solution:
2    def missingInteger(self, nums: List[int]) -> int:
3        res = nums[0]
4        n = len(nums)
5        seen = set(nums)
6
7        for i in range(1, n):
8            if nums[i] == nums[i - 1] + 1:
9                res += nums[i]
10            else:
11                break
12        
13        while res in seen:
14            res += 1
15        
16        return res
17
18