# Last updated: 10/14/2025, 10:33:18 PM
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
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

            if best >= k:
                return True
        return False



