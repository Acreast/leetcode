# Last updated: 10/14/2025, 9:57:26 PM
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        size = 1
        prev_size = 0
        max_size = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                size += 1
            else:
                prev_size = size
                size = 1
            max_size = max(max_size, max(size >> 1, min(prev_size, size)))
            if max_size >= k:
                return True
        return False



