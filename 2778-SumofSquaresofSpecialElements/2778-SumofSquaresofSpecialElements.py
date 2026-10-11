# Last updated: 10/11/2026, 9:13:10 PM
1class Solution:
2    def sumOfSquares(self, nums: List[int]) -> int:
3        res = 0
4        n = len(nums)
5        for i,num in enumerate(nums):
6            index_shift_1 = i + 1
7            if n % index_shift_1 == 0:
8                res += num * num
9        
10        return res