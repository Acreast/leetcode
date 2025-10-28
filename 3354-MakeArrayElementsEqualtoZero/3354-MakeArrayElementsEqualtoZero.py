# Last updated: 10/29/2025, 12:09:32 AM
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        N = len(nums)
        count = 0 
        left = 0
        right = sum(nums)
        for i in range(N):
            left += nums[i]
            right -= nums[i]
            if nums[i] != 0:
                continue
            if left == right:
                count += 2
            if abs(left - right) == 1:
                count += 1
        return count