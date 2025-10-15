# Last updated: 10/15/2025, 11:03:44 PM
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        size = 1
        prev_size = 0
        best = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                size += 1
            else:
                prev_size = size
                size = 1
            
            split_case = size // 2

            adjacent_case = min(prev_size, size)

            best = max(best, split_case, adjacent_case)

            
        return best
        