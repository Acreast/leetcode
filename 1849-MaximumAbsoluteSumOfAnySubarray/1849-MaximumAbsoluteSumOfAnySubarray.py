# Last updated: 7/12/2025, 11:49:28 PM
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        sum, minSum, maxSum = 0, 0, 0
        for num in nums:
            sum += num
            maxSum = max(maxSum, sum)
            minSum = min(minSum, sum)
        return abs(maxSum - minSum)