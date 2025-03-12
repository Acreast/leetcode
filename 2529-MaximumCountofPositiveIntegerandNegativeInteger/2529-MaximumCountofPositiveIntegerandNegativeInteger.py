class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative_count = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                negative_count += 1
                continue
            if nums[i] == 0:
                continue
            return max(negative_count, len(nums) - i)
        return negative_count       