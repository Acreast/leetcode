# Last updated: 9/30/2025, 11:17:15 PM
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        N = len(nums)
        while N != 1:
            for i in range(N - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            N -= 1
        
        return nums[0]