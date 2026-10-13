# Last updated: 10/13/2026, 10:55:28 PM
1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        for i, n in enumerate(nums):
4            nums[i] *= nums[i] 
5        
6        nums.sort()
7
8        n = len(nums)
9        half = n //2
10        res = 0
11        for i, n in enumerate(nums):
12            if i < half:
13                res -= n
14            else:
15                res += n
16        return res