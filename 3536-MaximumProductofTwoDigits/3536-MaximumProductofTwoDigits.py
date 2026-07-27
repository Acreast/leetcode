# Last updated: 7/27/2026, 9:31:35 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        max1, max2 = 0, 0
4        for num in nums:
5            if num > max1:
6                max2 = max1
7                max1 = num
8            elif num > max2:
9                max2 = num
10        
11        return (max1 - 1) * (max2 - 1)